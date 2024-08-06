from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64

def upload_file(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        fs = FileSystemStorage()
        filename = fs.save(csv_file.name, csv_file)
        uploaded_file_url = fs.url(filename)
        
        # Load CSV data into DataFrame
        data = pd.read_csv(fs.path(filename))
        
        # Data analysis
        first_rows = data.head().to_html(classes='table table-striped')
        summary_stats = data.describe().to_html(classes='table table-striped')
        
        # Handling missing values - Convert Series to DataFrame
        missing_values = data.isnull().sum().reset_index()
        missing_values.columns = ['Column', 'Missing Values']
        missing_values = missing_values.to_html(classes='table table-striped')

        # Filter numerical columns for correlation heatmap
        numeric_data = data.select_dtypes(include='number')
        
        plots = []
        if not numeric_data.empty:
            # Correlation heatmap
            plt.figure(figsize=(10, 8))
            sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm')
            plt.title('Correlation Heatmap')
            plots.append(get_plot_base64(plt))

            # Histograms for numerical columns
            for column in numeric_data.columns:
                plt.figure(figsize=(8, 6))
                sns.histplot(data[column], kde=True)
                plt.title(f'Histogram of {column}')
                plots.append(get_plot_base64(plt))

        context = {
            'first_rows': first_rows,
            'summary_stats': summary_stats,
            'missing_values': missing_values,
            'plots': plots
        }
        
        return render(request, 'analysis/results.html', context)
    return render(request, 'analysis/upload.html')

def get_plot_base64(plt):
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    return base64.b64encode(buf.read()).decode('utf-8')