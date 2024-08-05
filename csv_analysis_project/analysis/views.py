from django.shortcuts import render
from .forms import CSVUploadForm
from .models import CSVFile
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from django.conf import settings

# Function to generate histograms for numerical columns
def generate_histogram(data, column_name):
    plt.figure(figsize=(10, 6))
    sns.histplot(data[column_name], kde=True)
    plt.title(f'Distribution of {column_name}')
    plt.xlabel(column_name)
    plt.ylabel('Frequency')
    
    # Save the plot as an image file
    plot_path = os.path.join(settings.MEDIA_ROOT, f'{column_name}_histogram.png')
    plt.savefig(plot_path)
    plt.close()
    
    return plot_path

# Main view function to handle file upload and processing
def upload_file(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the uploaded file
            csv_file = form.save()
            
            # Read the CSV file into a DataFrame
            data = pd.read_csv(csv_file.file.path)
            
            # Perform data analysis
            data_head = data.head()
            summary_stats = data.describe()
            missing_values = data.isnull().sum()

            # Generate visualizations
            histograms = []
            for column in data.select_dtypes(include='number').columns:
                histograms.append(generate_histogram(data, column))

            # Add results and plots to the context
            context = {
                'data_head': data_head.to_html(),
                'summary_stats': summary_stats.to_html(),
                'missing_values': missing_values.to_html(),
                'histograms': histograms,  # List of file paths to histogram images
            }

            return render(request, 'analysis/result.html', context)
    else:
        form = CSVUploadForm()
    
    return render(request, 'analysis/upload.html', {'form': form})
