

# medical_summarizer/summarizer.py
import os
from tqdm import tqdm
from .config import Config
from .data_loader import create_dataloader
from .model import MedicalSummarizerModel
from .utils import setup_logging

class MedicalLectureSummarizer:
    def __init__(self, config=Config):
        self.config = config
        self.model = MedicalSummarizerModel(config.MODEL_NAME, config.MODEL_PATH)
        self.logger = setup_logging()

    def summarize_directory(self, input_dir, output_dir):
        os.makedirs(output_dir, exist_ok=True)
        dataloader = create_dataloader(input_dir, self.config.BATCH_SIZE, self.config.NUM_WORKERS)

        self.logger.info(f"Starting summarization of {len(dataloader.dataset)} lectures")
        for i, batch in enumerate(tqdm(dataloader)):
            summaries = self.model.summarize(
                batch,
                max_length=self.config.MAX_LENGTH,
                min_length=self.config.MIN_LENGTH,
                num_beams=self.config.NUM_BEAMS,
                no_repeat_ngram_size=self.config.NO_REPEAT_NGRAM_SIZE
            )

            for j, summary in enumerate(summaries):
                output_file = os.path.join(output_dir, f"summary_{i * self.config.BATCH_SIZE + j + 1}.txt")
                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(summary)

        self.logger.info(f"Summarization complete. Summaries saved in {output_dir}")
 
