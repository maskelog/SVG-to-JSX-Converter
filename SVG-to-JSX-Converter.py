import tkinter as tk
from tkinter import filedialog, ttk
from xml.dom import minidom
import os
import time

def clean_and_convert_svg(svg_filename, component_name):
    doc = minidom.parse(svg_filename)
    
    # 마스크 제거
    masks = doc.getElementsByTagName('mask')
    for mask in masks:
        mask.parentNode.removeChild(mask)
    
    # 불필요한 그룹 제거
    groups = doc.getElementsByTagName('g')
    for group in groups:
        if not group.hasChildNodes():
            group.parentNode.removeChild(group)
    
    # JSX로 변환
    svg_content = doc.getElementsByTagName('svg')[0].toxml()
    svg_content = svg_content.replace('xmlns="http://www.w3.org/2000/svg"', '')
    
    return f"export const {component_name}Icon = () => (\n    {svg_content}\n);\n"

def convert_svgs_to_jsx(progress_bar):
    svg_filenames = filedialog.askopenfilenames(filetypes=[("SVG files", "*.svg")])
    total_files = len(svg_filenames)
    
    if svg_filenames:
        output_jsx_filename = filedialog.asksaveasfilename(defaultextension=".jsx", filetypes=[("JSX files", "*.jsx")])
        if output_jsx_filename:
            jsx_components = []
            export_names = []
            for i, filename in enumerate(svg_filenames):
                component_name = os.path.basename(filename).split('_')[0].capitalize()
                jsx_components.append(clean_and_convert_svg(filename, component_name))
                export_names.append(f"{component_name}Icon")
                
                # Update progress bar
                progress_bar['value'] = (i+1)/total_files*100
                app.update_idletasks()
                time.sleep(0.1)  # Simulate time taken for conversion
            
            jsx_content = 'import React from \'react\';\n\n' + '\n\n'.join(jsx_components)
            jsx_content += f"\nexport default {{{', '.join(export_names)}}};\n"
            
            with open(output_jsx_filename, 'w') as f:
                f.write(jsx_content)
            progress_bar['value'] = 0  # Reset progress bar

app = tk.Tk()
app.title("SVGs to JSX Converter")

progress_bar = ttk.Progressbar(app, orient='horizontal', length=300, mode='determinate')
progress_bar.pack(pady=10)

convert_button = tk.Button(app, text="Convert SVGs to JSX", command=lambda: convert_svgs_to_jsx(progress_bar))
convert_button.pack(pady=20)

app.mainloop()