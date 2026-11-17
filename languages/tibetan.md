---
id: tibetan
title: Tibetan
kind: classical and modern
group: Tibetic
countries: [China, India, Nepal, Bhutan]
scripts: [Tibetan]
speakers: not verified
directory_names: [Tibetan, Classical Tibetan]
resource_level: low
google_translate: yes (since 2024)
recommendation: Google or Microsoft as a baseline with a human translator
confidence: low
updated: 2026-11
contributors: []
---

# Tibetan

Classical (literary) Tibetan is the language of the Kangyur, the Tengyur and most texts of Tibetan Buddhism. Modern Tibetan has several spoken varieties, mainly Central (Ü-Tsang), Amdo and Kham. Classical Tibetan has many Buddhist texts and tools, but AI translation into Tibetan is weak and no public test measures current AI models in this direction.

## Summary

| | |
| --- | --- |
| Where | Tibet and other Tibetan areas of China, and exile communities in India and Nepal |
| Speakers | not verified |
| Script | Tibetan script |
| AI resources | low |
| Google Translate | yes, added in June 2024 [1]; the Google Cloud API page did not list Tibetan when we read it [2] |
| Microsoft Translator | yes (code bo) [3] |
| Speech to text | Whisper lists Tibetan [10]; Meta Omnilingual ASR covers it [11] |
| Best evidence on translation quality | FLORES-200, NLLB and ChatGPT, 2023 [4] |

## Writing and text input

Tibetan uses the Tibetan script. It is in Unicode. We did not check the details of the Unicode block or of fonts in this research. Word segmentation tools (for example Botok) and transliteration tools (for example pyewts, for Wylie) are listed in the Directory below.

OCR for printed pecha, woodblock prints and manuscripts is well covered by BDRC, OpenPecha and Monlam AI models (see the Directory below).

## Data

Classical and Buddhist Tibetan has the most data. BDRC, OpenPecha, Esukhia (Derge Kangyur and Tengyur), 84000 and Dharmamitra share large corpora and parallel texts (see the Directory below).

General web text is small:

- FineWeb-2 has 155,315 Tibetan documents (389.13 MB) [12].
- MADLAD-400 has 6,200 Tibetan documents (88.7 million characters) [13].
- TIB-STC, the corpus behind the Sun-Shine model, has about 11 billion tokens (18 GB). It also has Tibetan versions of instruction and safety sets [8]. The license is not stated.

We did not research data for the Amdo or Kham varieties, in text or speech.

## Speech

- OpenAI Whisper lists Tibetan (bo) [10]. We found no published error rate for Tibetan.
- Meta Omnilingual ASR (November 2025) reports a character error rate (CER) of 2.6 for Tibetan, with 73.5 hours of training audio [11]. This test set is small and narrow. Do not read this number as real-world quality.
- OpenPecha and Monlam AI share Tibetan speech data, models and a speech-to-text benchmark (see the Directory below).

## Machine translation

**Support.** The Google Translate help page lists Tibetan among the languages added in June 2024 [1]. The Google Cloud Translation API page (updated 2026-11-10) did not list Tibetan when we read it with an automatic tool [2]. So the consumer app supports Tibetan, but API support is not confirmed. Microsoft Translator supports Tibetan [3]. Meta NLLB-200 covers Tibetan (bod_Tibt) [6].

**Benchmark: FLORES-200 devtest, English to Tibetan, chrF++ (higher is better).**

| System | Score | Year | Source |
| --- | --- | --- | --- |
| NLLB-200 MoE | 29.7 | 2022 model, tested 2023 | [4] |
| NLLB-200 (likely 3.3B; copy of the official file, model not verified) | 27.4 | 2022 | [5] |
| ChatGPT (gpt-3.5) 5-shot | 14.7 | 2023 | [4] |
| ChatGPT (gpt-3.5) 0-shot | 12.7 | 2023 | [4] |

Google Translate was not scored for Tibetan in that study [4]. These results are from 2023. Newer models (GPT-5, Claude 4.x and 5.x, Gemini 3) may be much better, but we found no public score for them. chrF++ scores can only be compared between systems in the same language and direction, not across languages.

**Benchmark: Tibetan understanding (not translation).** TLUE (2025) tested models with multiple-choice questions in Tibetan. On Ti-MMLU, where random guessing gives 25%, Claude 3.5 Sonnet scored 33.95, Gemini 1.5 Flash 30.14 and DeepSeek-V3 29.51. Most models scored near or below random [7]. These are early-2025 models.

**Vendor claim.** Monlam AI says its model Monlam Melong (update "Monlam Think", November 2025) scored 73% on 1,500 test questions and 71% on a Class 12 Tibetan exam, and that it beats Gemini, Claude and DeepSeek. The scores of the other models were not published, and there was no independent test [9].

**Classical Tibetan as a target.** We found no system and no test for translation into Classical Tibetan. Most Buddhist tools (Dharmamitra, MLotsawa) are built for Tibetan to English.

## AI projects

- Monlam AI (Dharamsala): translation, OCR, speech and the Monlam Melong model [9]. On Hugging Face, the Monlam AI organization page showed one public model, a Tibetan RoBERTa (fill-mask), when we read it [14].
- Sun-Shine: a Tibetan model based on Llama-3.1-8B, from UESTC, Tibet University and others [8].
- TLUE: a Tibetan understanding benchmark [7].

## Recommendation

To translate into modern Tibetan today, use Google Translate or Microsoft Translator as a baseline, and test Monlam AI and a current frontier model (GPT, Claude, Gemini) next to them. For Classical Tibetan, use AI only for a draft. A human translator (lotsawa) must lead. Confidence is low, because the only translation scores are from 2023 and no test uses Buddhist text.

Test first: run the FLORES+ devtest, English to Tibetan, with chrF++ on these systems, and ask a native reviewer to read 50 sentences from each. Then test a small Buddhist sample (for example, 20 short passages with a glossary). Tibetan is not yet measured on the BuddhistAI leaderboard.

<!-- in-directory:start -->
## In the Directory

Projects and datasets in the [Directory](../directory/README.md) that list Tibetan, Classical Tibetan. This list is made from the Directory data. To add an entry, [suggest it](https://github.com/BuddhistAI/knowledge-base/issues/new?template=add-to-directory.yml).

**Projects** (35)

- [Dharmamitra](https://dharmamitra.org/) (Dharmamitra team (UC Berkeley and partners)): Machine translation, grammar analysis and search for Buddhist source languages. Its MITRA models are published on Hugging Face.
- [84000](https://84000.co/) (84000): Translates the Tibetan Buddhist canon (Kangyur and Tengyur) into English. Publishes its TEI files and translation memory on GitHub, and a public position on AI translation of canonical texts.
- [Monlam AI](https://monlam.ai/) (Monlam): Tibetan AI tools in one web app - translation, speech to text, text to speech and OCR.
- [Dharmamitra dictionaries and lexicon](https://github.com/dharmamitra/dharmamitra-stardict-dictionaries) (Dharmamitra team): StarDict dictionaries and a lexicon built from Dharmamitra's parallel text collection.
- [Buddhist AI Translator (慧译通)](https://github.com/xr843/Buddhist-AI-Translator) (xr843 (community)): AI translator for Buddhist texts with support for Sanskrit, Pali and Tibetan terms.
- [BDRC - Buddhist Digital Resource Center](https://www.bdrc.io/) (BDRC): The largest digital library of Tibetan texts (scans, e-texts and catalog). In 2026 it started an initiative to build open Buddhist datasets for AI, and it publishes OCR models and datasets on Hugging Face.
- [OpenPecha](https://openpecha.org/) (OpenPecha (WeBuddhist)): Open Tibetan texts and the tools and datasets to work with them (OCR, speech, translation, outlines). Datasets and models are on Hugging Face.
- [WeBuddhist app](https://webuddhist.com/) (WeBuddhist): App that connects readers to Buddhist scriptures in several languages.
- [SuttaCentral](https://suttacentral.net/) (SuttaCentral): Early Buddhist texts with parallels across languages and many translations. Texts and parallels are on GitHub (sc-data).
- [DharmaNexus](https://dharmanexus.org/) (Dharmamitra team (successor of BuddhaNexus)): Finds parallel and similar passages across the Pali, Sanskrit, Tibetan and Chinese canons.
- [FoJin](https://fojin.app/) (xr843 (community)): Buddhist text platform with more than 10,000 texts from over 600 sources and search across languages.
- [Adarshah](https://adarshah.org/) (Dharma Treasure): Digital Tibetan canon (Kangyur and Tengyur) with search.
- [Lotsawa House](https://www.lotsawahouse.org/) (Lotsawa House): Translations of Tibetan Buddhist texts, often with the Tibetan source.
- [BDRC Tibetan OCR app](https://github.com/buda-base/tibetan-ocr-app) (BDRC): Offline app for Tibetan OCR. The models are on Hugging Face (BDRC/tibetan-ocr).
- [BDRC OCR and layout models](https://huggingface.co/BDRC) (BDRC): More than 40 models for Tibetan OCR, line and layout detection, script type and page orientation, with matching datasets.
- [Namgyal OCR](https://github.com/eric86y/Namgyal-OCR) (Tibetan Manuscript Project Vienna): OCR for Tibetan manuscripts.
- [EAP813 Siberian Buddhist book heritage](https://eap.bl.uk/node/3516) (Buryat State University; British Library Endangered Archives Programme): 334 digitized Buddhist manuscripts from private collections in Buryatia and Zabaikalsky Krai. The page does not list the languages.
- [EAP529 Dambadarjaa Monastery manuscripts](https://eap.bl.uk/node/3086) (Monsound and Vision Foundation; British Library Endangered Archives Programme): 51 Buddhist manuscripts (7,400 sheets, 1860s to 1920s) from a monastery in Mongolia. The page does not list the languages.
- [Botok](https://github.com/WeBuddhist/Botok) (WeBuddhist): Tibetan word tokenizer in Python.
- [pyewts](https://github.com/WeBuddhist/pyewts) (WeBuddhist): Converts Tibetan Unicode to and from Wylie (EWTS) transliteration.
- [bophono](https://github.com/Esukhia/bophono) (Esukhia): Tibetan phonetics engine in Python.
- [lucene-bo](https://github.com/buda-base/lucene-bo) (BDRC): Tibetan text analyzer for Lucene and Elasticsearch search.
- [OpenPecha speech models](https://huggingface.co/openpecha) (OpenPecha (WeBuddhist)): Tibetan speech-to-text models, including models for the teachings of specific teachers, with training data and a benchmark.
- [dharma-transcribe](https://github.com/retiform-labs/dharma-transcribe) (Retiform Labs (community)): Transcription pipeline for recorded Dharma teachings in several languages.
- [MITRA models (buddhist-nlp)](https://huggingface.co/buddhist-nlp) (Dharmamitra team): About 60 models for Buddhist languages - translation (Gemma, Qwen, NLLB and mBART based), embeddings, sentence alignment, tagging and OCR.
- [Tibetan BERT and RoBERTa models](https://huggingface.co/KoichiYasuoka/roberta-base-tibetan) (Koichi Yasuoka (Kyoto University)): Tibetan language models, with versions for part-of-speech tagging.
- [MLotsawa and Tibetan speech models](https://huggingface.co/billingsmoore) (billingsmoore (community)): Tibetan to English translation models (MLotsawa) and Tibetan speech recognition models, with open datasets.
- [Monlam Tibetan RoBERTa](https://huggingface.co/MonlamAI/tibetan_RoBERTa_S_e6) (Monlam AI): Tibetan masked language model (fill-mask).
- [Sun-Shine and TIB-STC](https://github.com/Vicentvankor/sun-shine) (UESTC, Tibet University and others): Tibetan language model based on Llama-3.1-8B, trained on TIB-STC, a Tibetan corpus of about 11 billion tokens. The repo says the code and model release is coming soon.
- [Dharmamitra Claude Code agent](https://github.com/dharmamitra/dharmamitra-claude-code-agent) (Dharmamitra team): Starter pack for agent-based translation, critical editions and finding parallel passages.
- [BuddhistAI skills](https://github.com/BuddhistAI/buddhist-skills) (BuddhistAI): The best measured skill for each Buddhist task, per language, plus shared community skills.
- [Intellexus](https://www.kc-tbts.uni-hamburg.de/projects/intellexus.html) (University of Hamburg, Reichman University and partners): EU-funded research project on AI for Buddhist texts in Sanskrit and Tibetan. Makers of DharmaBench.
- [Tsadra Dharma AI Project](https://www.tsadra.org/ai-tools-for-tibetan-buddhist-translation/) (Tsadra Foundation with Dharmamitra): Webinars, slides and case studies on using AI tools in Tibetan translation work, and a Discord community for Dharma translation and AI.
- [BuddhistAI benchmarks](https://buddhistai.github.io/buddhist-benchmarks/) (BuddhistAI): Open benchmarks and leaderboards for Buddhist tasks. Ranks models and skills by top performance and best value.
- [Awesome Tibetan NLP](https://github.com/tibetan-nlp/awesome-tibetan-nlp) (tibetan-nlp): List of Tibetan NLP tools and data.

**Datasets** (35)

- [DharmaBench](https://github.com/Intellexus-DSI/DharmaBench) (Intellexus (Reichman University, University of Hamburg)): 13 classification and span-detection tasks on Indian and Tibetan canonical texts, about 4,900 test items.
- [Bo-bench](https://huggingface.co/datasets/MonlamAI/Bo-bench-v1.0.0) (Monlam AI): Multiple-choice questions on Tibetan grammar, literature and history, written by subject experts, for evaluating Tibetan language models.
- [TLUE](https://arxiv.org/abs/2503.12051) (UESTC, Tibet University and others): 22,963 multiple-choice questions on general Tibetan knowledge, translated from Chinese benchmarks (no Buddhism category).
- [BDRC Tibetan OCR benchmark](https://huggingface.co/datasets/BDRC/tibetan-ocr-benchmark) (BDRC): Evaluation set for Tibetan OCR across many kinds of prints and manuscripts. Has a public leaderboard.
- [Tibetan OCR diagnostic benchmark](https://huggingface.co/datasets/BDRC/tibetan-ocr-diagnostic-benchmark) (BDRC): 604 synthetic Tibetan page images that change one difficulty at a time (for example rotation or page shape) to show where OCR breaks.
- [Tibetan metadata benchmark](https://huggingface.co/datasets/BDRC/Bo_metadata_benchmark) (BDRC): Tests how well models extract title, author, translator, date and other catalog data from the start and end of a Tibetan text.
- [AI text outline benchmark](https://huggingface.co/datasets/openpecha/ai-text-outline-benchmark) (OpenPecha): 124 Tibetan Buddhist texts with human-confirmed section breaks, for evaluating outline extraction.
- [Page-to-character outline benchmark](https://huggingface.co/datasets/BDRC/PageToChar-Outline-benchmark) (BDRC): Finds where a text starts and ends inside OCR pages when page-level outlines are turned into character-level ones.
- [Tibetan speech-to-text benchmark](https://huggingface.co/datasets/openpecha/tibetan-voice-benchmark) (Monlam AI and OpenPecha): Reviewed Tibetan speech transcripts from audio books, teachings and other sources, for evaluating speech recognition.
- [BuddhistAI TOC extraction benchmark](https://huggingface.co/datasets/BuddhistAI/toc-extraction-tibetan) (BuddhistAI): Table-of-contents extraction from Tibetan texts, with a scorer and leaderboard.
- [SuttaCentral data (sc-data)](https://github.com/suttacentral/sc-data) (SuttaCentral): Texts, translations and parallels behind SuttaCentral.
- [BoCorpus](https://huggingface.co/datasets/openpecha/BoCorpus) (OpenPecha): Classical Tibetan texts from several digital collections, for training language models.
- [Tibetan corpus (Derge Kangyur and Tengyur)](https://github.com/tokushige-koyasan/tibetan-corpus) (tokushige-koyasan (community)): Plain text of 3,452 Tibetan Buddhist texts from the Derge Kangyur and Tengyur.
- [Derge Kangyur and Tengyur e-texts](https://github.com/Esukhia/derge-kangyur) (Esukhia): Digital Derge Kangyur (and a Tengyur repo next to it).
- [84000 translation memory](https://github.com/84000/data-translation-memory) (84000): Tibetan source segments aligned with 84000's English translations.
- [84000 TEI translations](https://github.com/84000/data-tei) (84000): 84000's published translations in TEI XML.
- [MITRA parallel data](https://github.com/dharmamitra/mitra-parallel) (Dharmamitra team): Parallel sentence data from the Dharmamitra project.
- [Mitrasaṃgraha](https://huggingface.co/datasets/buddhist-nlp/mitrasamgraha-released-data-only) (Dharmamitra team): Released part of the Dharmamitra parallel data collection. The paper version on GitHub (dharmamitra/mitrasamgraha-dataset) has 391,548 Sanskrit-English pairs with a test set.
- [Tibetan-English sentence alignment](https://huggingface.co/datasets/buddhist-nlp/sentence-alignment-tib-eng) (Dharmamitra team): Aligned Tibetan and English sentences.
- [Tibetan to English, Spanish, French and German pairs](https://huggingface.co/datasets/billingsmoore/tibetan-to-english-translation-dataset) (billingsmoore (community)): Tibetan sentences paired with translations, with sister sets for Spanish, French and German and a phonetics set.
- [BDRC OCR transcriptions (several sets)](https://huggingface.co/BDRC) (BDRC): Page images with checked transcriptions from many sources (ACIP, Berkeley, Monlam AI handwritten, Palri Parkhang and more), as separate datasets.
- [TiBLAD - Tibetan Book Layout Analysis Dataset](https://huggingface.co/datasets/BDRC/TiBLAD) (BDRC): Tibetan book pages with layout regions marked.
- [OpenPecha OCR datasets](https://huggingface.co/openpecha) (OpenPecha): Line images and transcriptions from Kangyur and other prints and manuscripts (Lhasa, Lithang, Derge, Stok, Drutsa and more), plus line and layout annotation.
- [Tibetan voice datasets](https://huggingface.co/datasets/openpecha/tibetan_voice) (OpenPecha): Tibetan speech with transcripts, including teachings, audio books and more. Monlam AI also publishes Bo-voice.
- [Garchen Rinpoche teachings speech data](https://huggingface.co/datasets/openpecha/garchen_rinpoche_data) (OpenPecha): 5.6 hours of transcribed teachings by Garchen Rinpoche, for speech recognition of one teacher.
- [Tibetan quotation detection](https://huggingface.co/datasets/BDRC/Bo-Quotation-Dataset) (BDRC): 254 classical Tibetan books with 23,095 human-reviewed quotation spans, for finding quotations in commentaries.
- [Tibetan yigchung (small-print notes) detection](https://huggingface.co/datasets/BDRC/Bo-Yigchung-Dataset) (BDRC): 762 classical Tibetan books with marked spans of yigchung, the small-print notes written under or beside the main line.
- [Tibetan spelling correction](https://huggingface.co/datasets/BDRC/tibetan-spelling-correction-dataset) (BDRC): Sentence pairs of a first transcription and the reviewer's corrected version, from BDRC's double-annotation work.
- [Tibetan word segmentation](https://huggingface.co/datasets/billingsmoore/tibetan-word-segmentation-ds) (billingsmoore (community)): Expert word boundaries for 100 sentences of modern Lhasa Tibetan news speech.
- [Tibetan NER](https://huggingface.co/datasets/TibetanAI/TibetanAI_NERv1.0) (TibetanAI): Named entity data for Tibetan.
- [Tibetan normalisation test data](https://huggingface.co/datasets/pagantibet/Tibetan-normalisation-testdata) (pagantibet): Test data for normalising historical Tibetan spelling, with an abbreviation dictionary next to it.
- [Tibetan metadata extracted](https://huggingface.co/datasets/openpecha/tibetan-metadata-extracted) (OpenPecha): Catalog data extracted from Tibetan texts, with training sets for language models.
- [Tibetan outline boundary snippets](https://huggingface.co/datasets/openpecha/tibetan-outline-boundary-snippets-unique) (OpenPecha): Tibetan text snippets around outline boundaries, for finding where works start and end.
- [Buddhist Philosophy Graph](https://huggingface.co/datasets/joyboseroy/buddhist-philosophy-graph) (joyboseroy (community)): Knowledge graph of nine Buddhist schools, from Theravada to Tibetan Vajrayana. Every link cites a named text with a quote.
- [MITRA instruction data](https://huggingface.co/datasets/buddhist-nlp/mitra-instructions) (Dharmamitra team): Instruction data from the MITRA project.

<!-- in-directory:end -->

## Sources

1. [Google Translate Help: more than 100 new languages](https://support.google.com/translate/answer/15139004?hl=en), read 2026-11-17
2. [Google Cloud Translation: Language support](https://docs.cloud.google.com/translate/docs/languages), read 2026-11-17
3. [Microsoft Learn: Translator language support](https://learn.microsoft.com/en-us/azure/ai-services/translator/language-support), read 2026-11-17
4. [Robinson et al. 2023, ChatGPT MT: Competitive for High- (but Not Low-) Resource Languages, arXiv 2309.07423](https://arxiv.org/pdf/2309.07423), read 2026-11-17
5. [Copy of the NLLB-200 metrics file (Mara4444/MSc_Thesis)](https://raw.githubusercontent.com/Mara4444/MSc_Thesis/main/datasets/others/nllb_metrics.csv), read 2026-11-17
6. [NLLB-200 1.3B model card](https://huggingface.co/facebook/nllb-200-1.3B/raw/main/README.md), read 2026-11-17
7. [TLUE: Tibetan Language Understanding Evaluation, arXiv 2503.12051v3](https://arxiv.org/html/2503.12051v3), read 2026-11-17
8. [Sun-Shine, arXiv 2503.18288v3](https://arxiv.org/html/2503.18288v3), read 2026-11-17
9. [Voice for Tibet: Monlam Think, November 2025](https://voicefortibet.com/pioneering-tibetan-it-outfit-launches-monlam-think-claims-it-outperformed-global-ai-models-in-tibetan-language-20430.html) and [Yarloong](https://www.yarloong.com/monlam-melong-outperforms-global-ai-in-tibetan-language-tests-916.html), read 2026-11-17
10. [OpenAI Whisper tokenizer.py (language list)](https://raw.githubusercontent.com/openai/whisper/main/whisper/tokenizer.py), read 2026-11-17
11. [Meta Omnilingual ASR, per-language results (7B LLM-ASR)](https://raw.githubusercontent.com/facebookresearch/omnilingual-asr/main/per_language_results_table_7B_llm_asr.csv), read 2026-11-17
12. [FineWeb-2 README](https://huggingface.co/datasets/HuggingFaceFW/fineweb-2/blob/cab26bb3cab1ca7c26bb13a48f80fc3d2def4620/README.md), read 2026-11-17
13. [MADLAD-400 README](https://huggingface.co/datasets/allenai/MADLAD-400/blob/f8e5ab9b4c80d211822840f9e1f3fe8079bea053/README.md?code=true), read 2026-11-17
14. [Monlam AI on Hugging Face](https://huggingface.co/MonlamAI/models), read 2026-11-17
