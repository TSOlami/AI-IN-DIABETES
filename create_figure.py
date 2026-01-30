import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# Create figure
fig, ax = plt.subplots(1, 1, figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

# Define colors
color_data = '#E8F4F8'
color_feature = '#D4E6F1'
color_fusion = '#AED6F1'
color_model = '#85C1E2'
color_output = '#5DADE2'
color_challenge = '#FFE6E6'

# Title
ax.text(7, 9.5, 'Multimodal AI Pipeline for Diabetes Care', 
        ha='center', va='center', fontsize=16, fontweight='bold')

# Data Sources Layer
y_data = 8.0
box_width = 2.5
box_height = 0.8
spacing = 0.3

# Wearable Sensors
rect1 = FancyBboxPatch((0.5, y_data), box_width, box_height, 
                       boxstyle="round,pad=0.05", 
                       edgecolor='black', facecolor=color_data, linewidth=1.5)
ax.add_patch(rect1)
ax.text(0.5 + box_width/2, y_data + box_height/2, 'Wearable Sensors\n(CGM, Activity, HR)', 
        ha='center', va='center', fontsize=9, fontweight='bold')

# Retinal Imaging
rect2 = FancyBboxPatch((3.5, y_data), box_width, box_height, 
                       boxstyle="round,pad=0.05", 
                       edgecolor='black', facecolor=color_data, linewidth=1.5)
ax.add_patch(rect2)
ax.text(3.5 + box_width/2, y_data + box_height/2, 'Retinal Imaging\n(Fundus, OCT)', 
        ha='center', va='center', fontsize=9, fontweight='bold')

# EHR Data
rect3 = FancyBboxPatch((6.5, y_data), box_width, box_height, 
                       boxstyle="round,pad=0.05", 
                       edgecolor='black', facecolor=color_data, linewidth=1.5)
ax.add_patch(rect3)
ax.text(6.5 + box_width/2, y_data + box_height/2, 'Electronic Health\nRecords', 
        ha='center', va='center', fontsize=9, fontweight='bold')

# Genomic Data
rect4 = FancyBboxPatch((9.5, y_data), box_width, box_height, 
                       boxstyle="round,pad=0.05", 
                       edgecolor='black', facecolor=color_data, linewidth=1.5)
ax.add_patch(rect4)
ax.text(9.5 + box_width/2, y_data + box_height/2, 'Genomic Data\n(SNPs, PRS)', 
        ha='center', va='center', fontsize=9, fontweight='bold')

# Feature Extraction Layer
y_feature = 6.5
# LSTM/RNN
rect5 = FancyBboxPatch((0.5, y_feature), box_width, box_height, 
                       boxstyle="round,pad=0.05", 
                       edgecolor='black', facecolor=color_feature, linewidth=1.5)
ax.add_patch(rect5)
ax.text(0.5 + box_width/2, y_feature + box_height/2, 'LSTM/RNN\nTemporal Features', 
        ha='center', va='center', fontsize=9, fontweight='bold')

# CNN
rect6 = FancyBboxPatch((3.5, y_feature), box_width, box_height, 
                       boxstyle="round,pad=0.05", 
                       edgecolor='black', facecolor=color_feature, linewidth=1.5)
ax.add_patch(rect6)
ax.text(3.5 + box_width/2, y_feature + box_height/2, 'CNN\nImage Features', 
        ha='center', va='center', fontsize=9, fontweight='bold')

# Structured ML
rect7 = FancyBboxPatch((6.5, y_feature), box_width, box_height, 
                       boxstyle="round,pad=0.05", 
                       edgecolor='black', facecolor=color_feature, linewidth=1.5)
ax.add_patch(rect7)
ax.text(6.5 + box_width/2, y_feature + box_height/2, 'Gradient Boosting\nClinical Features', 
        ha='center', va='center', fontsize=9, fontweight='bold')

# Feature Engineering
rect8 = FancyBboxPatch((9.5, y_feature), box_width, box_height, 
                       boxstyle="round,pad=0.05", 
                       edgecolor='black', facecolor=color_feature, linewidth=1.5)
ax.add_patch(rect8)
ax.text(9.5 + box_width/2, y_feature + box_height/2, 'Feature Engineering\nGenetic Risk', 
        ha='center', va='center', fontsize=9, fontweight='bold')

# Arrows from data to features
for i, x_start in enumerate([0.5 + box_width/2, 3.5 + box_width/2, 6.5 + box_width/2, 9.5 + box_width/2]):
    arrow = FancyArrowPatch((x_start, y_data), (x_start, y_feature + box_height),
                           arrowstyle='->', mutation_scale=20, linewidth=2, color='gray')
    ax.add_patch(arrow)

# Fusion Layer
y_fusion = 5.0
fusion_width = 5.0
rect9 = FancyBboxPatch((4.5, y_fusion), fusion_width, box_height, 
                       boxstyle="round,pad=0.05", 
                       edgecolor='black', facecolor=color_fusion, linewidth=2)
ax.add_patch(rect9)
ax.text(4.5 + fusion_width/2, y_fusion + box_height/2, 'Multimodal Fusion\n(Attention, Cross-Modal Alignment)', 
        ha='center', va='center', fontsize=10, fontweight='bold')

# Arrows from features to fusion
for x_start in [0.5 + box_width/2, 3.5 + box_width/2, 6.5 + box_width/2, 9.5 + box_width/2]:
    arrow = FancyArrowPatch((x_start, y_feature), (7, y_fusion + box_height),
                           arrowstyle='->', mutation_scale=20, linewidth=1.5, color='gray')
    ax.add_patch(arrow)

# Predictive Models Layer
y_model = 3.5
model_width = 5.0
rect10 = FancyBboxPatch((4.5, y_model), model_width, box_height, 
                        boxstyle="round,pad=0.05", 
                        edgecolor='black', facecolor=color_model, linewidth=2)
ax.add_patch(rect10)
ax.text(4.5 + model_width/2, y_model + box_height/2, 'Predictive Models\n(Transformers, Ensemble Methods)', 
        ha='center', va='center', fontsize=10, fontweight='bold')

# Arrow from fusion to models
arrow = FancyArrowPatch((7, y_fusion), (7, y_model + box_height),
                       arrowstyle='->', mutation_scale=20, linewidth=2, color='gray')
ax.add_patch(arrow)

# Clinical Outputs Layer
y_output = 2.0
output_spacing = 3.5

# Glucose Prediction
rect11 = FancyBboxPatch((1.0, y_output), 2.8, box_height, 
                        boxstyle="round,pad=0.05", 
                        edgecolor='black', facecolor=color_output, linewidth=1.5)
ax.add_patch(rect11)
ax.text(1.0 + 1.4, y_output + box_height/2, 'Glucose Prediction\n& Hypoglycemia Alert', 
        ha='center', va='center', fontsize=8, fontweight='bold')

# DR Screening
rect12 = FancyBboxPatch((4.3, y_output), 2.8, box_height, 
                        boxstyle="round,pad=0.05", 
                        edgecolor='black', facecolor=color_output, linewidth=1.5)
ax.add_patch(rect12)
ax.text(4.3 + 1.4, y_output + box_height/2, 'DR Screening\n& Grading', 
        ha='center', va='center', fontsize=8, fontweight='bold')

# Risk Prediction
rect13 = FancyBboxPatch((7.6, y_output), 2.8, box_height, 
                        boxstyle="round,pad=0.05", 
                        edgecolor='black', facecolor=color_output, linewidth=1.5)
ax.add_patch(rect13)
ax.text(7.6 + 1.4, y_output + box_height/2, 'Complication Risk\nPrediction', 
        ha='center', va='center', fontsize=8, fontweight='bold')

# Arrows from models to outputs
for x_end in [1.0 + 1.4, 4.3 + 1.4, 7.6 + 1.4]:
    arrow = FancyArrowPatch((7, y_model), (x_end, y_output + box_height),
                           arrowstyle='->', mutation_scale=20, linewidth=1.5, color='gray')
    ax.add_patch(arrow)

# Challenges Box
y_challenge = 0.3
challenge_width = 12.0
rect14 = FancyBboxPatch((1.0, y_challenge), challenge_width, 0.9, 
                        boxstyle="round,pad=0.05", 
                        edgecolor='red', facecolor=color_challenge, linewidth=2)
ax.add_patch(rect14)
ax.text(1.0 + challenge_width/2, y_challenge + 0.45, 
        'Key Challenges: Temporal Alignment • Missing Modalities • Dataset Shift • Bias & Fairness • Interpretability • Deployment in Low-Resource Settings', 
        ha='center', va='center', fontsize=9, fontweight='bold', color='darkred')

plt.tight_layout()
plt.savefig('/home/sandbox/figures/multimodal_pipeline.pdf', dpi=300, bbox_inches='tight')
plt.savefig('/home/sandbox/figures/multimodal_pipeline.png', dpi=300, bbox_inches='tight')
print("Figure created successfully!")
