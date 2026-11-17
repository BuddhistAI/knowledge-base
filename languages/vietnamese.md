---
id: vietnamese
title: Vietnamese
kind: modern
group: Japanese, Korean, Vietnamese
countries: [Vietnam]
scripts: [Latin (Quốc ngữ), Hán-Nôm]
speakers: about 97 million (Ethnologue 2026)
speakers_n: 97000000
speakers_year: 2024
speakers_source: https://en.wikipedia.org/wiki/Vietnamese_language
directory_names: [Vietnamese, Hán-Nôm]
resource_level: high
google_translate: yes (Translation LLM and NMT)
recommendation: Frontier LLM with a Hán-Việt glossary and native review
confidence: low
updated: 2026-11
contributors: []
---

# Vietnamese

Vietnamese is the language of Vietnamese Buddhism, in Vietnam and in the diaspora (for example Plum Village). Older Buddhist texts are in Hán (Classical Chinese) and Nôm, together called Hán-Nôm. Short answer: AI handles modern Vietnamese well on general tests, but there is no translation benchmark like WMT for it. For Hán-Nôm, a Vietnamese system does OCR and transliteration.

## Summary

| | |
| --- | --- |
| Where | Vietnam and the diaspora |
| Speakers | about 97 million in total (Ethnologue 2026) [1] |
| Script | Latin alphabet (Quốc ngữ); Hán-Nôm in older texts |
| AI resources | high |
| Google Translate | yes, Translation LLM and NMT [2] |
| Microsoft Translator | yes, with LLM translation [3] |
| Speech to text | yes; Whisper large-v3 WER 8.9 on FLEURS [6] |
| Best evidence on translation quality | FLORES-200 (2023) [5]; no WMT test |

## Writing and text input

Modern Vietnamese uses the Latin alphabet with many diacritics. Unicode and input are mature. Spaces separate syllables, not words.

Hán-Nôm OCR: the "Kim Hán Nôm" system (Centre for Computational Linguistics, University of Science, VNU-HCM) reports over 95% accuracy on clean printed scans. Weathered inscriptions and handwriting still need experts. Its partners include the Tran Nhan Tong Institute, a Trúc Lâm Buddhist heritage institute [9]. An open OCR dataset (nom-ocr-data, 57.1k rows, CC BY 4.0) exists; it is not Buddhist [10]. The Vietnamese Nôm Preservation Foundation (1999–2018) worked on Nôm in Unicode and digitized texts, including at Thắng Nghiêm Temple [11]. We did not verify how many Nôm characters are in Unicode.

## Data

- The Kim Hán Nôm project reports 200,000 scanned pages, 750,000 Hán-Nôm–Quốc ngữ sentence pairs and over 1 million Hán-Nôm sentences. Release terms are not stated [9].
- Vĩnh Nghiêm pagoda holds 3,050 woodblocks of the Trúc Lâm Zen school (UNESCO Memory of the World Asia-Pacific, 2012). We found no digitization of them [12].
- Small community datasets on Hugging Face: a Buddhism Q&A set in Vietnamese and English (MIT) [16], and a Thich Nhat Hanh dataset with no license and no description [17].
- Chinese canon text from CBETA uses CC BY-NC-SA 4.0 with extra conditions. This limits commercial model training [18].
- We found no open, aligned Vietnamese Buddhist corpus.

## Speech

- Whisper supports Vietnamese [8].
- **Benchmark**: Whisper large-v3 word error rate (lower is better) is 8.9 on FLEURS and 14.8 on Common Voice 17 (2025 study) [6].
- Omnilingual ASR (2025) reports CER 5.4 [7].
- A feasibility study plans a system for Thich Nhat Hanh's teachings with transcribed audio and video. It does not say whether anything was built [19].

## Machine translation

**Benchmark, FLORES-200, English to Vietnamese, chrF++ (higher is better)**: NLLB about 59.3 [4]; in 2023 NLLB-MoE 59.5 and ChatGPT 0-shot 58.5 [5]. This is high, but chrF++ cannot be compared across languages.

There is no WMT human evaluation for Vietnamese. **Indirect benchmark**: in a 2026 study, normalizing dialect text raised acceptance of Gemini 2.0 Flash translations from 61.83% to 67.00% [15]. **Benchmark (knowledge, not translation)**: on VMLU, a Vietnamese multiple-choice test, Llama-3-70B scored 66.44 and GPT-4 65.53 (2024) [14].

We found no Buddhist test into Vietnamese. Older results may not show what current models can do.

## Classical form: Hán-Nôm

- Kim Hán Nôm reports over 99% accuracy for transliteration from Hán-Nôm to Quốc ngữ on clean digital text. Translation of meaning for Hán texts is planned for a later phase, so it is not yet mature [9].
- VanMach-7B is a community model for reading Chữ Nôm and Hán-Nôm. No evaluation is reported [13].
- Buddhist terms in Vietnamese are often Hán-Việt words, for example "duyên khởi" and "chân như". This is a natural bridge from Classical Chinese.

## AI projects

- **Kim Hán Nôm** (VNU-HCM): OCR, transliteration, web, mobile apps and API [9].
- **tnh-scholar**: feasibility study for search, chat and translation of Thich Nhat Hanh's teachings [19].

## Recommendation

- **Into Vietnamese**: use a current frontier model, with a glossary of Hán-Việt Buddhist terms and a native reviewer. Gemini has slightly more indirect evidence, but no direct comparison exists.
- **From Hán-Nôm**: use Kim Hán Nôm for OCR and transliteration, then an LLM for meaning, with expert review.
- **Confidence: low.** There is no translation benchmark with human ratings and no Buddhist test.
- **First test**: take about 30 Buddhist passages with existing Vietnamese translations. Compare 3 models. Ask a native reviewer to mark errors in Hán-Việt terms.

<!-- in-directory:start -->
## In the Directory

Projects and datasets in the [Directory](../directory/README.md) that list Vietnamese, Hán-Nôm. This list is made from the Directory data. To add an entry, [suggest it](https://github.com/BuddhistAI/knowledge-base/issues/new?template=add-to-directory.yml).

**Projects** (2)

- [Kim Hán Nôm](https://kimhannom.fit.hcmus.edu.vn/) (University of Science, VNU-HCM (Center for Computational Linguistics)): OCR for printed and handwritten Hán and Nôm texts (Buddhist scripture is one document type), transliteration into Quốc ngữ and experimental translation. Web, mobile apps and API.
- [Gemma-SEA-LION-v4-27B-IT](https://huggingface.co/aisingapore/Gemma-SEA-LION-v4-27B-IT) (AI Singapore): Gemma 3 based 27B chat model for Southeast Asian languages, including Burmese, Khmer, Lao, Thai and Vietnamese. Not Buddhist-specific.

**Datasets** (1)

- [Vietnamese Buddhism Q&A](https://huggingface.co/datasets/vanloc1808/buddism-qa-dataset) (vanloc1808 (community)): Questions and answers on Buddhism in English and Vietnamese, merged from two source sets (about 16,000 rows in the dataset viewer).

<!-- in-directory:end -->

## Sources

1. [Wikipedia: List of languages by total number of speakers (Ethnologue 2026)](https://en.wikipedia.org/wiki/Languages_by_total_speakers), read 2026-11-17
2. [Google Cloud Translation: Language support](https://docs.cloud.google.com/translate/docs/languages), read 2026-11-17
3. [Microsoft Learn: Translator language support](https://learn.microsoft.com/en-us/azure/ai-services/translator/language-support), read 2026-11-17
4. [NLLB metrics, public copy (Mara4444/MSc_Thesis)](https://raw.githubusercontent.com/Mara4444/MSc_Thesis/main/datasets/others/nllb_metrics.csv), read 2026-11-17
5. [Robinson et al. 2023, ChatGPT MT, arXiv 2309.07423](https://arxiv.org/pdf/2309.07423), read 2026-11-17
6. [Dolphin paper, arXiv 2503.20212](https://arxiv.org/pdf/2503.20212), read 2026-11-17
7. [Omnilingual ASR per-language results (7B LLM-ASR)](https://raw.githubusercontent.com/facebookresearch/omnilingual-asr/main/per_language_results_table_7B_llm_asr.csv), read 2026-11-17
8. [openai/whisper tokenizer.py](https://raw.githubusercontent.com/openai/whisper/main/whisper/tokenizer.py), read 2026-11-17
9. [HCMUS: AI unlocks Hán Nôm heritage, 2026-07-19](https://en.hcmus.edu.vn/ai-unlocks-han-nom-heritage-opening-the-door-to-a-millennium-of-knowledge-for-wider-public-access/), read 2026-11-17
10. [nom-ocr-data on Hugging Face](https://huggingface.co/datasets/aerbote88/nom-ocr-data), read 2026-11-17
11. [Wikipedia: Vietnamese Nôm Preservation Foundation](https://en.wikipedia.org/wiki/Vietnamese_N%C3%B4m_Preservation_Foundation), read 2026-11-17
12. [Vietnam Government portal: Vĩnh Nghiêm woodblocks, 2012-05-17](https://en.baochinhphu.vn/vinh-nghiem-woodblocks-become-world-documentary-heritage-11113452.htm), read 2026-11-17
13. [VanMach-7B on Hugging Face](https://huggingface.co/Duyu/VanMach-7B), read 2026-11-17
14. [VMLU on GitHub](https://github.com/ZaloAI-Jaist/VMLU/), read 2026-11-17
15. [ViDia2Std, arXiv 2603.10211](https://arxiv.org/html/2603.10211), read 2026-11-17
16. [vanloc1808/buddism-qa-dataset](https://huggingface.co/datasets/vanloc1808/buddism-qa-dataset/tree/main), read 2026-11-17
17. [nphuc/thich-nhat-hanh-dataset](https://huggingface.co/datasets/nphuc/thich-nhat-hanh-dataset/tree/main), read 2026-11-17
18. [CBETA Copyright Notice](https://cbeta.org/en/copyright), read 2026-11-17
19. [tnh-scholar preliminary feasibility study](https://aaronksolomon.github.io/tnh-scholar/preliminary_feasibility_study), read 2026-11-17
