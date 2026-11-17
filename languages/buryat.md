---
id: buryat
title: Buryat
kind: modern
group: Mongolic and Turkic
countries: [Russia, Mongolia, China]
scripts: [Cyrillic]
speakers: 130,500 to 440,000; sources disagree (2010 census and Wikipedia infobox [1])
directory_names: [Buryat]
resource_level: very low
google_translate: yes (since 2024)
recommendation: Google Translate or Yandex compared with a frontier LLM on a small test
confidence: low
updated: 2026-11
contributors: []
---

# Buryat

Buryat is a Mongolic language of Buryatia (Russia) and of Buryats in Mongolia and Inner Mongolia. The Buddhist manuscripts we found from Buryatia are in Tibetan and Classical Mongolian, and Russian is the common working language for modern Buddhist material. Google and Yandex translate into Buryat, but there is no independent test of their quality.

## Summary

| | |
| --- | --- |
| Where | Republic of Buryatia and nearby areas of Russia; at least 100,000 Buryats in Mongolia and Inner Mongolia [1] |
| Speakers | sources disagree: 440,000 native speakers (infobox, 2017–2020, no source named); 353,113 speakers in the 2002 Russian census; 130,500 speakers in the Republic of Buryatia in the 2010 census [1] |
| Script | Cyrillic since 1939; earlier Classical Mongolian script [1] |
| AI resources | very low |
| Google Translate | yes, added 27 June 2024 [2][3]; Google Cloud: NMT only [4] |
| Microsoft Translator | no [5] |
| Speech to text | not in Whisper [6] or Omnilingual ASR [7] |
| Best evidence on translation quality | small study of an NLLB fine-tune (2025), BLEU [8][9] |

## Writing and text input

Buryat uses Cyrillic with three extra letters (Ү, Ө, Һ) [1]. Before 1939 Buryats wrote in the Classical Mongolian script. The Vagindra script (Agvan Dorzhiev, 1905) was never widely used [1]. We did not test OCR; check that tools handle the extra letters.

Activists say Russian census language data overstate real language use [10].

## Data

- **Buryat–Russian parallel corpus** (Sarana Abidueva): 10,000 to 100,000 sentence pairs, CC BY 4.0 [11].
- **Buryat monolingual corpus** (same author): size and license not verified [12].
- Buddhist manuscripts (images, research use only): **EAP813** (Buryat State University, 2015): about 1,000 Buddhist manuscripts found in Buryatia and Aga, 334 digitized [13]. **EAP1034** (from 2017, Ulan-Ude and Aga monastery): 107 volumes of the Chone canon and 293 xylographs, in Tibetan [14].

We found no Buddhist text in modern Buryat as a dataset. Buryat is not among the FLORES-200 languages in the 2023 comparison study [15], so there are no comparable FLORES numbers.

## Speech

Whisper has no Buryat code [6], and Omnilingual ASR has no Buryat row [7]. A 2025 paper describes speaker-dependent Buryat speech recognition; no data or model is stated as available [16].

## Machine translation

**Products.** Google Translate added Buryat on 27 June 2024 [2][3]. Google's Cloud page lists Buryat (code `bua`) for the older NMT engine only, not for its Translation LLM [4]. Yandex Translate added Buryat in October 2025, built with data from the Buryat "Belig" language centre [17]. Microsoft does not list Buryat [5]. We found no published quality numbers for these products.

**Research (benchmark, small).** The two sources for the same NLLB-200 fine-tune give different numbers:

| Source | Russian → Buryat | Buryat → Russian | Metric |
| --- | --- | --- | --- |
| FieldMatters 2025 paper [8] | about 20 | about 35 | BLEU |
| Hugging Face model card (MIT) [9] | about 13 | about 20 | BLEU |

The paper also says native speakers rated the output as acceptable [8]. BLEU numbers can only be compared between systems in the same language and direction.

We found no test of GPT, Claude or Gemini translating into Buryat.

## AI projects

- Sarana Abidueva and colleagues: Buryat corpora and the NLLB-200 Buryat–Russian model [8][9][11].
- Yandex, with the Belig centre [17].
- ai-forever has an mGPT model for Kalmyk and lists sibling Buryat and Tuvan models [18].

## Recommendation

To translate into Buryat today, use Google Translate or Yandex as a baseline, and compare them with a frontier LLM on a small test. For Buddhist material, translating from Russian may work better than from English, because most parallel data is Buryat–Russian [11]. A native speaker must post-edit all output.

Confidence: **low**. The products exist, but there is no independent quality test, and the only research numbers disagree.

First test: take 50 sentences of Buddhist prose in Russian. Translate them into Buryat with Google Translate, Yandex and one or two frontier LLMs. Ask two native speakers to rank the outputs and mark errors in Buddhist terms.

<!-- in-directory:start -->
## In the Directory

Projects and datasets in the [Directory](../directory/README.md) that list Buryat. This list is made from the Directory data. To add an entry, [suggest it](https://github.com/BuddhistAI/knowledge-base/issues/new?template=add-to-directory.yml).

**Projects** (1)

- [NLLB-200 Buryat-Russian](https://huggingface.co/SaranaAbidueva/nllb-200-bxr-ru) (Sarana Abidueva): NLLB-200 fine-tuned for Buryat-Russian translation. Reported BLEU is about 13 (Russian to Buryat) and 20 (Buryat to Russian).

**Datasets** (1)

- [Buryat-Russian parallel corpus](https://huggingface.co/datasets/SaranaAbidueva/buryat-russian_parallel_corpus) (Sarana Abidueva): Buryat-Russian sentence pairs (10,000 to 100,000), used to train an NLLB-200 Buryat model.

<!-- in-directory:end -->

## Sources

1. [Wikipedia: Buryat language](https://en.wikipedia.org/wiki/Buryat_language), read 2026-11-17
2. [Google Translate Help: more than 100 new languages](https://support.google.com/translate/answer/15139004?hl=en), read 2026-11-17
3. [RFE/RL, 28 June 2024: Google Translate adds 110 languages](https://www.rferl.org/a/google-translate-adds-110-languages-including-mother-tongues-russia/33012893.html), read 2026-11-17
4. [Google Cloud Translation: language support](https://docs.cloud.google.com/translate/docs/languages), read 2026-11-17
5. [Microsoft Learn: Translator language support](https://learn.microsoft.com/en-us/azure/ai-services/translator/language-support), read 2026-11-17
6. [openai/whisper tokenizer.py (language list)](https://raw.githubusercontent.com/openai/whisper/main/whisper/tokenizer.py), read 2026-11-17
7. [Omnilingual ASR per-language results (7B LLM-ASR)](https://raw.githubusercontent.com/facebookresearch/omnilingual-asr/main/per_language_results_table_7B_llm_asr.csv), read 2026-11-17
8. [Baturova et al., FieldMatters 2025](https://preview.aclanthology.org/setup/2025.fieldmatters-1.8), read 2026-11-17
9. [SaranaAbidueva/nllb-200-bxr-ru model card](https://huggingface.co/SaranaAbidueva/nllb-200-bxr-ru/blame/main/README.md), read 2026-11-17
10. [The Moscow Times, 2023](https://www.themoscowtimes.com/all/80432), read 2026-11-17
11. [SaranaAbidueva/buryat-russian_parallel_corpus](https://huggingface.co/datasets/SaranaAbidueva/buryat-russian_parallel_corpus/tree/refs%2Fconvert%2Fparquet/default/train), read 2026-11-17
12. [SaranaAbidueva/buryat_monocorpus](https://huggingface.co/datasets/SaranaAbidueva/buryat_monocorpus/tree/main), read 2026-11-17
13. [British Library EAP813](https://eap.bl.uk/node/3516), read 2026-11-17
14. [Culture in Crisis: Preserving traditional Buryat book culture](https://cultureincrisis.org/projects/preserving-traditional-buryat-book-culture), read 2026-11-17
15. [Robinson et al. 2023, ChatGPT MT, arXiv 2309.07423 (FLORES-200 language list)](https://arxiv.org/pdf/2309.07423), read 2026-11-17
16. [Chimitov and Zavyalova 2025, Amur State University journal](https://lingua.amursu.ru/en/about-journal/volumes/2025/2/2025-2-13), read 2026-11-17
17. [www1.ru: Yandex adds Buryat, 25 October 2025](https://www1.ru/en/news/2025/10/25/iandeks-rassiriaet-gorizonty-v-perevodcike-osvoen-buriatskii-iazyk.html), read 2026-11-17
18. [ai-forever/mGPT-1.3B-kalmyk model card](https://huggingface.co/ai-forever/mGPT-1.3B-kalmyk/raw/main/README.md), read 2026-11-17
