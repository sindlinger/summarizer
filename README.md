
# README.md 
# Advanced Medical Lecture Summarizer 
 
This project provides a comprehensive solution for summarizing medical lectures using the Flan-T5-Large model. It's designed for medical residency students to efficiently process and summarize lecture materials. 
 
## Features 
-	Automatic downloading and setup of the Flan-T5-Large model 
-	Efficient tokenization and batching of input texts 
-	Customizable summarization parameters 
-	Progress tracking and logging 
-	Multithreaded processing for improved performance 
 
## Installation 
1.	Clone the repository:    ```    git clone https://github.com/your-username/advanced-medical-lecturesummarizer.git    cd advanced-medical-lecture-summarizer 
   ``` 
 
2.	Create a virtual environment and install dependencies:    ```    python -m venv .venv    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`    pip install -r requirements.txt 
   ``` 
 
3.	Download the model: 
   ``` 
   python scripts/download_model.py 
   ``` 
 
## Usage 
Run the summarization script: 
``` python scripts/run_summarization.py --input_dir /path/to/lectures --output_dir /path/to/summaries 
