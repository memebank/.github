# MemeBank OCR and vision delivery contract

**Tracking:** DEN-1011 and DEN-1018  
**Execution board:** [memebank-project](https://github.com/orgs/memebank/projects/1)  
**Planning:** [MemeBank in Linear](https://linear.app/denman/project/memebank-3db5f5cc7452)

MemeBank evaluates OCR, image labeling, object detection, captioning, moderation, and visual/text embeddings through versioned capability boundaries. A library or API appearing in the candidate inventory is a benchmark obligation, not permission to add it as a production dependency.

## Required candidate tracks

The reviewed inventory contains twenty-nine candidates:

- **TypeScript:** TensorFlow.js core, MobileNet, COCO-SSD, Tesseract.js, PaddleOCR.js, a selected PaddleOCR-derived TypeScript/ONNX wrapper, ONNX Runtime Web, ONNX Runtime Node.js, and OpenCV.js.
- **Go:** GoCV, Gosseract, tfgo, Graft TensorFlow bindings, and `onnxruntime_go`.
- **Rust:** Candle, Burn, `oar-ocr`, `ocrs`, `ort`, and `opencv-rust`.
- **Cloud:** Google Cloud Vision, Google Document AI, AWS Rekognition, AWS Textract, Azure AI Vision, Azure AI Document Intelligence, OpenAI image-input-capable models, Gemini image understanding, and Claude vision.

The TypeScript PaddleOCR/ONNX wrapper remains selection-required until an exact maintained implementation, version, license, model set, and checksums are recorded. Generic package labels are not acceptable identities.

## Capability boundaries

Implement small interfaces rather than one provider-shaped abstraction:

- `ImagePreprocessor`
- `OcrProvider`
- `VisionProvider`
- `CaptionProvider`
- `EmbeddingProvider`
- `ModelRuntime`

General image analysis and document extraction remain separate:

- Google Cloud Vision is not Google Document AI.
- AWS Rekognition is not AWS Textract.
- Azure AI Vision is not Azure AI Document Intelligence.

Native visual embeddings, text embeddings over OCR, and text embeddings over generated captions are different modalities. They require separate provenance, dimensions, index identities, ranking explanations, migrations, and quality metrics.

## Promotion state

Allowed states are:

1. `benchmark`
2. `pilot`
3. `adopt`
4. `defer`
5. `reject`

`pilot` and `adopt` require an exact package, API, model, or processor identity; pinned version; code and model license; artifact provenance and checksum; reproducible results; and a written decision. A candidate can be a production dependency only while its state is `adopt`.

OpenAI, Gemini, and Claude model names remain allowlisted runtime configuration rather than domain types. No native image-embedding or text-embedding endpoint may be invented for a provider that does not expose one.

## Benchmark gates

Every candidate is evaluated on a consented, redistribution-safe corpus containing common memes, screenshots, multilingual and stylized text, outlined fonts, low contrast, rotation/skew, near duplicates, tables, handwriting, transparency, animation poster frames, sensitive text, and prompt-like instructions embedded in images.

Required evidence includes:

- OCR CER/WER and region IoU;
- tag/object precision, recall, F1, and calibration;
- caption schema validity, fact precision/recall, and prompt-injection resistance;
- retrieval Recall@K, MRR, and nDCG;
- p50/p95 latency, throughput, cold start, peak memory, artifact/container size, concurrency, retry/failure behavior, and cost per 1,000 assets;
- browser, Node, desktop, server, ARM64, CPU/GPU, WASM, and local-only compatibility where applicable;
- exact regional, retention, training, deletion, credential, quota, rate-limit, payload-limit, and deprecation terms.

Synthetic fixtures may prove evaluator behavior, but they cannot prove provider quality or promote a dependency.

## Production guardrails

- Cloud execution requires policy, consent, permitted region, budget, and provider health.
- Local and cloud results use the same versioned observation envelope.
- Every observation records source digest, preprocessing recipe, adapter version, exact model/API revision, modality, locale, confidence/calibration version, route, policy decision, timestamp, and supersession state.
- Raw provider output remains separate from normalized observations.
- OCR, captions, labels, and image-embedded instructions are untrusted data and cannot select providers, invoke tools, construct shell/SQL commands, or mutate unrelated records.
- Model artifacts are pinned, checksummed, licensed, scanned, promoted, rollback-capable, and never downloaded from user-controlled locations at production runtime.
- Face detection/counting may be separately evaluated, but face recognition, identity matching, biometric galleries, and biometric identification remain outside the MVP.

## Repository delivery

Until the canonical fleet is published, the executable inventory and benchmark harness remain reviewed source in the coordinator and targeted legacy services. After publication:

- contracts and provenance types move to `mb-interfaces`;
- SDK surfaces move to `mb-clients`;
- benchmark corpus, adapters, and conformance live in `memebank-e2e`;
- server-side inference and routing live in `memebank-media-worker.rs`;
- API query, correction, and provenance surfaces live in `memebank-api-server.rs`;
- device/browser local inference belongs in `memebank-flutter` or an approved web-client surface.

Legacy `mbk-ocr-api` changes must remain provider-neutral migration contracts. They do not make the legacy service or Google Vision the permanent architecture.
