---
id: mongolian
title: Mongolian
kind: classical and modern
group: Mongolic and Turkic
countries: [Mongolia, China, Russia]
scripts: [Cyrillic, Traditional Mongolian, Clear Script]
speakers: about 5 million native speakers (2020 to 2022; Wikipedia [1])
speakers_n: 5000000
speakers_year: 2022
speakers_source: https://en.wikipedia.org/wiki/Mongolian_language
speakers_basis: first-language speakers
directory_names: [Mongolian, Classical Mongolian]
resource_level: medium
google_translate: yes (Cyrillic only)
recommendation: Frontier LLM (Gemini first) in Cyrillic with native review
confidence: medium
updated: 2026-11
contributors: []
---

# Mongolian

Mongolian is the language of Buddhism in Mongolia and among Mongols in Inner Mongolia (China). This page covers modern Khalkha Mongolian in Cyrillic, Mongolian in the traditional vertical script, Classical Mongolian (the language of the Mongolian Kanjur) and the Oirat Clear Script. Large AI models handle Cyrillic Mongolian quite well, but they are much weaker in the traditional script.

## Summary

| | |
| --- | --- |
| Where | Mongolia; Inner Mongolia (China); Russia [1] |
| Speakers | about 5 million native speakers (2020–2022); nearly 3.6 million in Mongolia (2014 estimate). No reliable count for Inner Mongolia [1] |
| Script | Cyrillic (Mongolia), traditional Mongolian script (China and Mongolia), Clear Script (Oirats in Xinjiang) [1] |
| AI resources | medium (Cyrillic); low (traditional script and Classical Mongolian) |
| Google Translate | yes, Cyrillic; Google Cloud: Translation LLM "experimental" [2] |
| Microsoft Translator | yes, Cyrillic and traditional script [3] |
| Speech to text | Whisper lists Mongolian [4]; open ASR is weak (WER 64.9) [5] |
| Best evidence on translation quality | FLORES-200 (2023) [6]; knowledge tests of frontier LLMs (2026) [7][8] |

## Writing and text input

Cyrillic Mongolian has no special Unicode problem. In March 2020 the government announced plans to use both Cyrillic and traditional script in official documents by 2025 [1]. We did not verify if this became law.

The traditional script is in the Unicode Mongolian block (U+1800–U+18AF). Letters that look the same are told apart with free variation selectors. There are known rendering and line-break problems [9][10]. Clear Script (Todo), Manchu and Sibe letters are in the same block [9]. A Cyrillic-to-traditional converter exists at trans.mglip.com [11].

OCR and handwriting: MOLHW has 164,631 online handwriting samples of the traditional script; the best model had a word error rate of 16.97% [12]. We found no OCR for Mongolian Kanjur woodblock pages or for Clear Script.

## Data

- **Mongolian Kanjur** (108 volumes, Classical Mongolian, translated from Tibetan): India's National Mission for Manuscripts reprinted it; copies were presented to Mongolia in July 2020. No e-text is mentioned [13]. We found no openly licensed machine-readable Mongolian Kanjur or Tanjur.
- **National Library of Mongolia** (BDRC and ACIP, from 2018): more than 31,000 uncatalogued volumes. The source describes Tibetan-language texts [14].
- **EAP529** (British Library): 51 manuscripts (7,400 sheets, 1860s–1920s) from Dambadarjaa Monastery; research use only [15].
- **Tohoku University dictionaries**: searchable scans of historical Mongolian dictionaries and an Oirat (Clear Script) dictionary [16].
- **MonCulture-Eval** built parallel traditional/Cyrillic items; experts corrected 14.2% of back-translated segments [7].

## Speech

- SpeechBrain Whisper-large-v2 fine-tuned on Common Voice 10 (Mongolian): word error rate 64.92, character error rate 25.73; Apache-2.0 [5].
- Omnilingual ASR (Meta, November 2025): Mongolian (Cyrillic) character error rate 5.5, with 28.2 hours of training data [17]. Test sets differ between languages; do not compare languages with this number.
- MnTTS and MnTTS2: open Mongolian text-to-speech datasets from Inner Mongolia University [18].
- Vendor claims (no quality numbers): Chimege Systems (Mongolia) [19], Speechmatics and ElevenLabs.

## Machine translation

**FLORES-200, English → Mongolian (Cyrillic), chrF++** [6]: Google Translate 49.8, NLLB-200 (MoE) 43.9, ChatGPT (gpt-3.5) 5-shot 26.6. These are 2023 results; newer models may be much better. chrF++ can only be compared between systems in the same language and direction.

**Knowledge tests, not translation tests (benchmark):**

- MonCulture-Eval (Findings of ACL 2026), 2,911 culture items, factual accuracy in traditional / Cyrillic script: Gemini-3-Pro-Preview 79.5 / 76.7; GPT-5.2 40.4 / 60.5; Qwen3-Max 44.6 / 58.8; Claude-Sonnet-4.5 33.3 / 56.5; DeepSeek-v3.2 28.9 / 48.4. The authors say most models show "a sharp performance decline in the Traditional script" [7].
- "Left Behind" (2026): frontier models averaged 87.3% on Mongolian tasks, against 92.2% in English [8].

**Anecdotal:** in 2018, Google Translate's Mongolian service produced widely reported mistranslations [20]. This is old.

Yandex Translate also supports Mongolian [21]. No published test uses Buddhist text.

## AI projects

- **Egune AI** (Mongolia): Mongolian AI models; raised US$3.5 million in May 2025. Model details not verified [22].
- **Chimege Systems**: Mongolian speech recognition [19].
- Inner Mongolia University (MnTTS) [18] and Minzu University of China (MonCulture-Eval) [7] work on the traditional script.

## Recommendation

To translate into Cyrillic Mongolian today, use a frontier LLM, with Gemini 3 Pro as the first choice, and native review. For the traditional script, translate into Cyrillic first, then convert with a dedicated converter or test Microsoft Translator's traditional-script option, and have an expert check the result. For Classical Mongolian, there is no tested system.

Confidence: **medium** for Cyrillic (strong 2026 knowledge tests, but no recent translation test); **low** for the traditional script and Classical Mongolian.

First test: take 50 to 100 sentences of Buddhist prose with a trusted Mongolian translation. Translate with Gemini, one other frontier model and Google Translate. Score with chrF++ and ask a reviewer to check Buddhist terms. Then convert the best output to the traditional script and check the rendering.

<!-- in-directory:start -->
## In the Directory

Projects and datasets in the [Directory](../directory/README.md) that list Mongolian, Classical Mongolian. This list is made from the Directory data. To add an entry, [suggest it](https://github.com/BuddhistAI/knowledge-base/issues/new?template=add-to-directory.yml).

**Projects** (1)

- [EAP529 Dambadarjaa Monastery manuscripts](https://eap.bl.uk/node/3086) (Monsound and Vision Foundation; British Library Endangered Archives Programme): 51 Buddhist manuscripts (7,400 sheets, 1860s to 1920s) from a monastery in Mongolia. The page does not list the languages.

**Datasets** (0)

None listed yet.

<!-- in-directory:end -->

## Sources

1. [Wikipedia: Mongolian language](https://en.wikipedia.org/wiki/Mongolian_language), read 2026-11-17
2. [Google Cloud Translation: language support](https://docs.cloud.google.com/translate/docs/languages), read 2026-11-17
3. [Microsoft Learn: Translator language support](https://learn.microsoft.com/en-us/azure/ai-services/translator/language-support), read 2026-11-17
4. [openai/whisper tokenizer.py (language list)](https://raw.githubusercontent.com/openai/whisper/main/whisper/tokenizer.py), read 2026-11-17
5. [SpeechBrain asr-whisper-large-v2-commonvoice-mn](https://huggingface.co/speechbrain/asr-whisper-large-v2-commonvoice-mn/blob/main/README.md?code=true), read 2026-11-17
6. [Robinson et al. 2023, ChatGPT MT, arXiv 2309.07423, Table 11](https://arxiv.org/pdf/2309.07423), read 2026-11-17
7. [MonCulture-Eval, Findings of ACL 2026](https://aclanthology.org/2026.findings-acl.1449.pdf), read 2026-11-17
8. ["Left Behind", arXiv 2603.21036](https://arxiv.org/pdf/2603.21036), read 2026-11-17
9. [Wikipedia: Mongolian (Unicode block)](https://en.wikipedia.org/wiki/Mongolian_(Unicode_block)), read 2026-11-17
10. [Unicode Technical Report 54](https://www.unicode.org/reports/tr54/tr54-1.html), read 2026-11-17
11. [Language Log, 3 August 2024](https://languagelog.ldc.upenn.edu/nll/?p=65244), read 2026-11-17
12. [Pan et al., MOLHW, Scientific Reports 2023](https://www.nature.com/articles/s41598-022-27267-8), read 2026-11-17
13. [Drishti IAS: Mongolian Kanjur being reprinted](https://www.drishtiias.com/daily-updates/daily-news-analysis/mongolian-kanjur-being-reprinted/print_manually), read 2026-11-17
14. [BDRC: Digitizing the National Library of Mongolia](https://bdrc.io/2018/09/11/digitizing-the-national-library-of-mongolia), read 2026-11-17
15. [British Library EAP529](https://eap.bl.uk/node/3086), read 2026-11-17
16. [Digital Orientalist: Tohoku online dictionaries of Mongolian](https://digitalorientalist.com/2020/10/02/digitizing-the-mongolian-language-an-introduction-to-the-polyglot-online-dictionaries-and-full-text-search-of-mongolian-languages-and-written-manchu/), read 2026-11-17
17. [Omnilingual ASR per-language results (7B LLM-ASR)](https://raw.githubusercontent.com/facebookresearch/omnilingual-asr/main/per_language_results_table_7B_llm_asr.csv), read 2026-11-17
18. [MnTTS, arXiv 2209.10848](https://arxiv.org/pdf/2209.10848), read 2026-11-17
19. [Inside Mongolia: Chimege Systems](https://www.insidemongolia.mn/post/DhMAL5TWkEo), read 2026-11-17
20. [The Diplomat, 2018: Google Translate's Mongolia service](https://thediplomat.com/2018/01/google-translates-mongolia-service-goes-horribly-wrong), read 2026-11-17
21. [www1.ru: Yandex adds Buryat, 25 October 2025](https://www1.ru/en/news/2025/10/25/iandeks-rassiriaet-gorizonty-v-perevodcike-osvoen-buriatskii-iazyk.html), read 2026-11-17
22. [The AI Insider: Egune AI secures $3.5M](https://theaiinsider.tech/2025/05/20/egune-ai-secures-3-5m-to-advance-national-ai-infrastructure-in-mongolia/), read 2026-11-17
