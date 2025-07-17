# QA Synthetic Data Generation with YData

This repository provides a pipeline to generate high-quality **synthetic question-answer pairs** from documents using the **YData synthetic data platform**. The resulting dataset is suitable for training and evaluating **Large Language Models (LLMs)** for Document Question Answering (QA) tasks.

## 📌 Overview

Legal datasets are often sensitive, proprietary, or limited in scope, making it challenging to train robust QA systems. This project leverages **YData’s generative capabilities** to create **privacy-preserving**, **statistically valid**, and **domain-specific synthetic datasets**.

## 🔍 Use Case

This synthetic dataset can be used to train and fine-tune LLMs (such as GPT, LLaMA, or BERT variants) for tasks including:

- Contract clause QA
- Regulatory document analysis
- Legal research automation
- Compliance checking
- Interactive legal assistants

Due to unavailability of credits, the project was terminated with the demo of just one capability.

## 🧱 Features

- 📄 Ingests structured or unstructured legal documents
- 💬 Generates realistic QA pairs mimicking legal language
- 🔐 Ensures data privacy and compliance
- ⚙️ Built using YData's Python library

## 📦 Requirements

- Python 3.10+
- ydata-sdk[text, docx]
- pandas