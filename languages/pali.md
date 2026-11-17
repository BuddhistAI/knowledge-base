---
id: pali
title: Pali
kind: classical
group: Indic
countries: [Sri Lanka, Myanmar, Thailand, Cambodia, Laos]
scripts: [Roman, Sinhala, other Theravada scripts]
speakers: not applicable (liturgical language)
directory_names: [Pali]
resource_level: very low
google_translate: no
recommendation: Frontier LLM with a glossary and a Pali reviewer
confidence: low
updated: 2026-11
contributors: []
---

# Pali

Pali is the language of the Theravada canon (Tipitaka) and its commentaries. It has rich, open text corpora, but no translation service supports it, and no public test measures translation into Pali.

## Summary

| | |
| --- | --- |
| Where | Theravada countries and Pali students worldwide |
| Speakers | not applicable (liturgical and scholarly language) |
| Script | Roman for international use; Sinhala script in Sri Lanka; other local scripts |
| AI resources | very low (for translation and speech); text corpora are good |
| Google Translate | no [1] [2] |
| Microsoft Translator | no [3] |
| Speech to text | not in Whisper [4]; not in Meta Omnilingual ASR [5] |
| Best evidence on translation quality | PaliBench, Pali to English only, 2026 [6] |

## Writing and text input

Pali has no script of its own. Sri Lankan readers use the Sinhala script, and international readers use Roman letters with diacritics. Tools in the Directory (for example paliscript and "Tipitaka Pali in 15 scripts") convert between scripts. So an AI system can write Roman Pali, and a tool can convert it to the reader's script.

OCR: a Sinhala and Pali OCR model and its training data (pathnirvana) are listed in the Directory below.

## Data

- The canon and commentaries are open: SuttaCentral, Tipitaka.org (Chaṭṭha Saṅgāyana), Tipitaka.lk and the Digital Pāḷi Dictionary are listed in the Directory below.
- Parallel text: SuttaCentral has Pali aligned segment by segment with English translations by Bhikkhu Sujato, which are CC0 [6].
- PaliBench uses 1,700 passages (8,389 segments, about 345,000 tokens) from three Nikāyas, each with three English translations. The licenses differ: Sujato CC0, Thanissaro CC BY-NC 4.0, Bodhi CC BY-NC-ND 3.0 [6]. Bodhi's translations do not allow derivatives, so be careful when you train or share data built from them.
- Dharmamitra's MITRA mined corpus does not include Pali. Pali appears only as 149,418 Pali–English pairs in its pretraining data [7].

## Speech

- OpenAI Whisper does not list Pali [4].
- Meta Omnilingual ASR has no Pali language code [5].
- We found no public Pali chanting dataset with transcripts. One idea is to start from a Sinhala or Thai speech model with a Pali word list, but this is not tested.

## Machine translation

**Support.** Google Translate does not support Pali [1] [2]. Microsoft Translator does not support Pali [3]. Pali is not in the FLORES-200 test set, so there are no FLORES scores for any system [8].

**Benchmark (opposite direction): PaliBench, Pali to English, 10 models through OpenRouter, January–February 2026.** Gemini 3 Pro scored best (similarity 0.946, chrF++ 68.5, BLEU 63.3, higher is better). Gemini 3 Flash scored 0.944 and Claude Opus 4.5 0.940. DeepSeek v3.2 scored 0.939, and GPT-5.2 was also tested. LLaMA 3.3 70B was last (0.888) [6].

These numbers are for translation **from** Pali. A model that reads Pali well does not always write good Pali. We found no test of translation **into** Pali by any system.

**MITRA.** Dharmamitra's MITRA-MT model (Gemma 2, 9B) translates into English. Its paper reports no scores for translation into Pali [7].

## AI projects

- PaliBench: a multi-reference Pali to English benchmark (May 2026). Code: github.com/MateMetzger/palibench; the license is not stated [6].
- Dharmamitra: MITRA models and data, with some Pali in pretraining [7].
- SuttaCentral, the Digital Pāḷi Dictionary and Sri Lankan Tipitaka sites are listed in the Directory below.

## Recommendation

To translate into Pali today, use a current frontier model (Gemini 3 Pro and Claude Opus scored best on PaliBench, but only from Pali into English). Give it a glossary from the Digital Pāḷi Dictionary and similar SuttaCentral passages as examples. Ask it to write Roman Pali, then convert the script with a tool. A trained Pali reviewer must check every sentence. Confidence is low, because there is no test in this direction.

Test first: take 50 to 100 SuttaCentral segments with Sujato's CC0 English translation. Give the model the English and ask for Pali. Score the output against the original Pali with chrF++, and ask a Pali scholar to review 20 items. Pali is not yet measured on the BuddhistAI leaderboard.

<!-- in-directory:start -->
## In the Directory

Projects and datasets in the [Directory](../directory/README.md) that list Pali. This list is made from the Directory data. To add an entry, [suggest it](https://github.com/BuddhistAI/knowledge-base/issues/new?template=add-to-directory.yml).

**Projects** (21)

- [Dharmamitra](https://dharmamitra.org/) (Dharmamitra team (UC Berkeley and partners)): Machine translation, grammar analysis and search for Buddhist source languages. Its MITRA models are published on Hugging Face.
- [Digital Pāḷi Dictionary](https://www.dpdict.net/) (Digital Pāḷi Dictionary team): Pali to English dictionary with grammar data and a compound splitter. The full database is on GitHub.
- [Buddhist AI Translator (慧译通)](https://github.com/xr843/Buddhist-AI-Translator) (xr843 (community)): AI translator for Buddhist texts with support for Sanskrit, Pali and Tibetan terms.
- [BDRC - Buddhist Digital Resource Center](https://www.bdrc.io/) (BDRC): The largest digital library of Tibetan texts (scans, e-texts and catalog). In 2026 it started an initiative to build open Buddhist datasets for AI, and it publishes OCR models and datasets on Hugging Face.
- [SuttaCentral](https://suttacentral.net/) (SuttaCentral): Early Buddhist texts with parallels across languages and many translations. Texts and parallels are on GitHub (sc-data).
- [DharmaNexus](https://dharmanexus.org/) (Dharmamitra team (successor of BuddhaNexus)): Finds parallel and similar passages across the Pali, Sanskrit, Tibetan and Chinese canons.
- [FoJin](https://fojin.app/) (xr843 (community)): Buddhist text platform with more than 10,000 texts from over 600 sources and search across languages.
- [Tipitaka.lk](https://tipitaka.lk/) (Path Nirvana): The Buddha Jayanthi Tipitaka of Sri Lanka with its Sinhala translation, plus other Pali editions.
- [Tipitaka.org (Chaṭṭha Saṅgāyana)](https://www.tipitaka.org/) (Vipassana Research Institute): The Pali canon of the Sixth Council in many scripts.
- [Digital Pali Reader](https://digitalpalireader.online/) (Digital Pali Reader project): Pali canon reader with built-in dictionary lookup.
- [GRETIL](https://gretil.sub.uni-goettingen.de/) (Göttingen State and University Library): Collection of Sanskrit and other Indic e-texts, including many Buddhist texts.
- [Thai Tipitaka program](https://sourceforge.net/p/thaitipitaka) (ajsun and bistechn (community)): Desktop program with the Thai Royal, Mahachula and Mahamakut Thai Tipitaka editions and two Pali editions in Thai script.
- [BUDSIR](https://www.mahidol.ac.th/budsir/history.htm) (Mahidol University): Search system for the Pali Tipitaka and commentaries in Thai and Roman script, in use since 1988.
- [Tipitaka Sajjhaya](https://sajjhaya.org/node/20) (World Tipitaka Foundation (Bangkok)): The Sixth Council Pali Tipitaka in Roman script, with notation for recitation and audio recordings.
- [Sinhala and Pali OCR model](https://huggingface.co/pathnirvana/sinhala-pali-ocr-lightonocr-1b) (Path Nirvana): OCR model for old Sinhala and Pali prints, trained on its own open dataset.
- [Pali script tools (paliscript)](https://github.com/5w0rdf15h/paliscript) (5w0rdf15h (community)): Python library and command line tool for Pali transliteration between Thai, Sinhala, Roman and other scripts.
- [SuttaCentral Voice](https://github.com/sc-voice/sc-voice) (SuttaCentral Voice): Reads suttas from SuttaCentral aloud with text-to-speech.
- [MITRA models (buddhist-nlp)](https://huggingface.co/buddhist-nlp) (Dharmamitra team): About 60 models for Buddhist languages - translation (Gemma, Qwen, NLLB and mBART based), embeddings, sentence alignment, tagging and OCR.
- [Dharmamitra Claude Code agent](https://github.com/dharmamitra/dharmamitra-claude-code-agent) (Dharmamitra team): Starter pack for agent-based translation, critical editions and finding parallel passages.
- [Tripitaka MCP server](https://github.com/dhamma-seeker/tripitaka-mcp) (dhamma-seeker (community)): Gives AI assistants access to the full Pali Tipiṭaka (about 444,000 segments, aligned with SuttaCentral).
- [SuttaCentral awesome list](https://github.com/suttacentral/awesome) (SuttaCentral): Projects built on SuttaCentral texts and data.

**Datasets** (12)

- [PaliBench](https://github.com/MateMetzger/palibench) (Máté Metzger with Mahachulalongkornrajavidyalaya University): Pali to English translation benchmark of 1,700 passages with several reference translations, with scores for 10 LLMs. The repo has code, prompts and scores, but not the Pali passages or the reference translations.
- [SuttaCentral data (sc-data)](https://github.com/suttacentral/sc-data) (SuttaCentral): Texts, translations and parallels behind SuttaCentral.
- [Early Buddhist Texts, Pali and English](https://huggingface.co/datasets/linhgiang/early-buddhist-texts) (linhgiang (community)): 5,764 suttas of the Pali Sutta Piṭaka aligned segment by segment with Bhikkhu Sujato's English translations.
- [Pali Tipitaka in Thai script](https://huggingface.co/datasets/uisp/pali-tripitaka-thai-script-siamrath-version) (uisp (community)): The Pali Tipitaka (Siamrath edition) in Thai script, with a matching commentary set.
- [Tipitaka Pali in 15 scripts](https://huggingface.co/datasets/freococo/tipitaka_pali_in_15_scripts) (freococo (community)): The Pali Tipitaka written in 15 scripts.
- [SiPaKosa](https://github.com/RanxduG/SiPaKosa-Dataset) (RanxduG (community)): Corpus of canonical and classical Buddhist texts in Sinhala and Pali.
- [Tipitaka in Myanmar script (DatarrX)](https://huggingface.co/datasets/DatarrX/tipitaka-dataset) (DatarrX (community)): Pali Mula, Atthakatha and Tika texts in Myanmar script, about 463,000 paragraphs as JSON.
- [Pali Tripitaka parallel corpus](https://github.com/x39826/Pali_Tripitaka) (x39826 (community)): Pali scriptures as used in 15 countries, with a parallel corpus.
- [Sinhala and Pali OCR data](https://huggingface.co/datasets/pathnirvana/sinhala-pali-ocr) (Path Nirvana): Old Sinhala and Pali prints with transcriptions.
- [Buddhist Philosophy Graph](https://huggingface.co/datasets/joyboseroy/buddhist-philosophy-graph) (joyboseroy (community)): Knowledge graph of nine Buddhist schools, from Theravada to Tibetan Vajrayana. Every link cites a named text with a quote.
- [Dhamma.Gift definitions](https://huggingface.co/datasets/dhammagift/dg-dataset) (Dhamma.Gift): Key terms of the suttas with the definitions the suttas themselves give.
- [INNER ATLAS SuttaCentral quotations](https://huggingface.co/datasets/Zaneoiji/inneratlas-suttacentral) (Zaneoiji (community)): 703,068 quotation records from SuttaCentral texts in many languages, each with its own rights and attribution.

<!-- in-directory:end -->

## Sources

1. [Google Translate Help: more than 100 new languages](https://support.google.com/translate/answer/15139004?hl=en), read 2026-11-17
2. [Google Cloud Translation: Language support](https://docs.cloud.google.com/translate/docs/languages), read 2026-11-17
3. [Microsoft Learn: Translator language support](https://learn.microsoft.com/en-us/azure/ai-services/translator/language-support), read 2026-11-17
4. [OpenAI Whisper tokenizer.py (language list)](https://github.com/openai/whisper/blob/main/whisper/tokenizer.py), read 2026-11-17
5. [Meta Omnilingual ASR language IDs](https://raw.githubusercontent.com/facebookresearch/omnilingual-asr/main/src/omnilingual_asr/models/wav2vec2_llama/lang_ids.py), read 2026-11-17
6. [Metzger and Phophichit, PaliBench, arXiv 2605.16881, 2026-05-16](https://arxiv.org/pdf/2605.16881), read 2026-11-17
7. [Nehrdich and Keutzer, MITRA, arXiv 2601.06400, 2026-01-10](https://arxiv.org/pdf/2601.06400), read 2026-11-17
8. [Robinson et al. 2023, arXiv 2309.07423](https://arxiv.org/pdf/2309.07423), read 2026-11-17
