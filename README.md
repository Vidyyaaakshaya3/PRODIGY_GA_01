---

# 🎬 Fine-Tuning GPT-2 for Movie Recommendations

## 📌 Internship Task - Prodigy InfoTech (Generative AI Intern)

As part of my internship at *Prodigy InfoTech, I worked on a Generative AI project where I **fine-tuned a pre-trained GPT-2 model on a custom movie dataset* to generate human-like movie recommendations. The task was designed to help me understand how to structure textual data, tokenize it, fine-tune a language model, and generate contextually relevant output based on user preferences.

---

## 🛠 Implementation Overview

✅ *Dataset Preparation*  
- Created a simple movie dataset with titles, genres, years, and runtimes.  
- Formatted data into natural language prompts for model training.

✅ *Text Generation for Training*  
- Converted structured movie data into descriptive sentences like:  
  “I recommend Titanic, a drama and romance movie from 1997.”

✅ *Model Fine-Tuning*  
- Used HuggingFace’s GPT2LMHeadModel and Trainer API to fine-tune GPT-2 on custom movie recommendation texts.  
- Implemented tokenization, input preparation, and trained the model for 1 epoch.

✅ *Recommendation System*  
- Developed a simple interface where users can input genre-based queries (e.g., “horror movies”) and receive AI-generated movie suggestions.  
- Cleaned and matched outputs with the original movie dataset for more readable results.

---

## 🖼 Output Screenshot

> 📷 Below is a screenshot of the final working output of the model with real-time user queries:

![Final Output](https://github.com/Vidyyaaakshaya3/PRODIGY_GA_01/blob/main/GA_Task_1_output.png)
---

## 📚 References

- [#1 GeeksforGeeks - Conditional GANs](https://www.geeksforgeeks.org/deep-learning/conditional-generative-adversarial-network/)  
- [#2 Medium - How cGANs Work](https://scribe.rip/cgan-conditional-generative-adversarial-network-how)

---
