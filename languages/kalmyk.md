---
id: kalmyk
title: Kalmyk
kind: modern
group: Mongolic and Turkic
countries: [Russia]
scripts: [Cyrillic, Clear Script]
speakers: about 110,000 (2021 Russian census; Wikipedia [1])
directory_names: [Kalmyk]
resource_level: very low
google_translate: no
recommendation: Frontier LLM with full native post-editing
confidence: low
updated: 2026-11
contributors: []
---

# Kalmyk

Kalmyk (Kalmyk Oirat) is a Mongolic language of the Republic of Kalmykia in Russia. No major translation service supports it, and there is no translation test. A native speaker must lead any translation work. Russian is the common working language.

## Summary

| | |
| --- | --- |
| Where | Republic of Kalmykia, Russia [1] |
| Speakers | 110,000 in the 2021 Russian census, ethnic population 178,000 [1]; a model card says "about 0.2 million" [2] |
| Script | Cyrillic today; Clear Script (Todo bichig) until 1924 [1] |
| AI resources | very low |
| Google Translate | no [3][4] |
| Microsoft Translator | no [5] |
| Speech to text | not in Whisper [6]; Omnilingual ASR covers Kalmyk [7] |
| Best evidence on translation quality | none found |

## Writing and text input

Modern Kalmyk is written in Cyrillic. The Clear Script was created by Zaya Pandita in the 17th century. Kalmyks used it until 1924, and Oirats in China still use it [1]. Clear Script letters are in the Unicode Mongolian block [8]. We found no OCR for Clear Script.

Activists say Russian census language data overstate real language use [9].

## Data

- **INEL Kalmyk Corpus** v1.0 (University of Hamburg, July 2025): 55 spoken texts, 2,076 sentences, 19,742 tokens, about 4 hours 23 minutes of audio (Derbet and Torgut dialects, recorded 2007–2018). It is glossed and has English and Russian translations. License CC BY-NC-SA 4.0 [10]. This is the only Kalmyk–Russian aligned text we verified.
- Studies of Kalmyk Buddhist manuscripts in Clear Script appear in the open-access journals of KIGIRAN (Elista) [11]. We found no machine-readable Kalmyk Buddhist corpus.

Kalmyk is not among the FLORES-200 languages in the 2023 comparison study [12]. We did not verify whether the newer FLORES+ includes Kalmyk.

## Speech

- Omnilingual ASR (Meta, November 2025): Kalmyk (`xal_Cyrl`) character error rate 2.3, with 41.4 hours of training data [7]. This very low error rate probably reflects a small and narrow test set. Do not read it as real-world quality, and do not compare languages with it.
- The INEL Kalmyk audio is also listed on Mozilla Data Collective [13].

## Machine translation

**Products.** Google Translate did not include Kalmyk in its 2024 expansion [3][4]. Microsoft does not list Kalmyk [5]. A 2025 report on Yandex Translate did not name Kalmyk among its languages of Russia [14]. We found no dedicated Kalmyk translation product.

**Research.** We found no translation benchmark and no published translation scores for Kalmyk. ai-forever's mGPT-1.3B-kalmyk is a language model, not a translation system (MIT license, tuned for 200 steps) [2].

**Anecdotal.** None found.

## AI projects

- INEL project, University of Hamburg (corpus) [10].
- ai-forever mGPT-1.3B-kalmyk [2].
- We found no Kalmyk speech or translation project beyond these.

## Recommendation

To translate into Kalmyk today, the only route is a frontier LLM, with a native speaker who post-edits every sentence. Translating from Russian may be easier for reviewers, because Russian is the common working language. Using Cyrillic Mongolian or Buryat as a guide for terms is possible, but untested.

Confidence: **low**. There is no product and no test.

First test: take 30 to 50 sentences of Buddhist prose in Russian. Ask two or three frontier LLMs to translate them into Kalmyk. Ask two native speakers to rate each sentence (usable, needs editing, wrong) and to mark invented words or words from Mongolian or Russian. If no model is usable, plan human translation.

<!-- in-directory:start -->
## In the Directory

Projects and datasets in the [Directory](../directory/README.md) that list Kalmyk. This list is made from the Directory data. To add an entry, [suggest it](https://github.com/BuddhistAI/knowledge-base/issues/new?template=add-to-directory.yml).

**Projects** (0)

None listed yet.

**Datasets** (1)

- [INEL Kalmyk Corpus](https://www.fdr.uni-hamburg.de/record/17676) (Universität Hamburg (INEL project)): 55 spoken Kalmyk texts (19,742 tokens, about 4.4 hours of audio), glossed, with Russian and English translations.

<!-- in-directory:end -->

## Sources

1. [Wikipedia: Kalmyk Oirat](https://en.wikipedia.org/wiki/Kalmyk_Oirat), read 2026-11-17
2. [ai-forever/mGPT-1.3B-kalmyk model card](https://huggingface.co/ai-forever/mGPT-1.3B-kalmyk/raw/main/README.md), read 2026-11-17
3. [Google Translate Help: more than 100 new languages](https://support.google.com/translate/answer/15139004?hl=en), read 2026-11-17
4. [Google Cloud Translation: language support](https://docs.cloud.google.com/translate/docs/languages), read 2026-11-17
5. [Microsoft Learn: Translator language support](https://learn.microsoft.com/en-us/azure/ai-services/translator/language-support), read 2026-11-17
6. [openai/whisper tokenizer.py (language list)](https://raw.githubusercontent.com/openai/whisper/main/whisper/tokenizer.py), read 2026-11-17
7. [Omnilingual ASR per-language results (7B LLM-ASR)](https://raw.githubusercontent.com/facebookresearch/omnilingual-asr/main/per_language_results_table_7B_llm_asr.csv), read 2026-11-17
8. [Wikipedia: Mongolian (Unicode block)](https://en.wikipedia.org/wiki/Mongolian_(Unicode_block)), read 2026-11-17
9. [The Moscow Times, 2023](https://www.themoscowtimes.com/all/80432), read 2026-11-17
10. [University of Hamburg FDR: INEL Kalmyk Corpus](https://www.fdr.uni-hamburg.de/record/17676), read 2026-11-17
11. [KIGIRAN Mongolian Studies journal, example article](https://mongoloved.kigiran.com/jour/article/download/1423/864), read 2026-11-17
12. [Robinson et al. 2023, ChatGPT MT, arXiv 2309.07423](https://arxiv.org/pdf/2309.07423), read 2026-11-17
13. [Mozilla Data Collective: INEL Kalmyk speech](https://prod.datacollective.mozillafoundation.org/datasets/cmn4kxlaj001xnz07a5yugnew), read 2026-11-17
14. [www1.ru: Yandex adds Buryat, 25 October 2025](https://www1.ru/en/news/2025/10/25/iandeks-rassiriaet-gorizonty-v-perevodcike-osvoen-buriatskii-iazyk.html), read 2026-11-17
