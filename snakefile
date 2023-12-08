rule prepare:
  output:
    "data/wine.zip",
    "data/wine/Index",
    "data/wine/wine.data",
    "data/wine/wine.names"
  shell:
    "python scripts/prepare_data.py"

rule profile:
  input:
    "data/wine/wine.data"
  output:
    "profiling/report.html"
  shell:
    "python scripts/profile.py"

rule analyze:
  input:
    "data/wine/wine.data"
  output:
    "results/correlation_heatmap.png",
    "results/distribution_plot.png",
    "results/violin_plot.png",
    "results/pairplot.png"
  shell:
    "python scripts/analysis.py"

rule reproduce:
  input:
    "profiling/report.html",
    "results/correlation_heatmap.png",
    "results/distribution_plot.png",
    "results/violin_plot.png",
    "results/pairplot.png"

  


