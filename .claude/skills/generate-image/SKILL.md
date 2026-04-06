---
name: generate-image
description: Generate images using the Gemini Nano Banana 2 API and save them as optimised JPGs
user_invocable: true
arguments:
  - name: prompt
    description: The image generation prompt
    required: true
  - name: filename
    description: Output filename (saved to images/ directory, e.g. hero-secretariat.jpg)
    required: true
  - name: aspect_ratio
    description: "Aspect ratio (default: 16:9). Options: 1:1, 16:9, 4:3, 3:4, 9:16"
    required: false
---

# Generate Image with Nano Banana 2

Generate an image using the Gemini Nano Banana 2 API (model: `gemini-3.1-flash-image-preview`) and save it as an optimised JPG in the project's `images/` directory.

## Steps

1. **Source the API key** from `secrets.env` in the project root:
   ```bash
   source secrets.env
   ```

2. **Call the Gemini API** using curl:
   ```bash
   curl -s -X POST \
     "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-image-preview:generateContent" \
     -H "x-goog-api-key: $GEMINI_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{
       "contents": [{
         "parts": [
           {"text": "<PROMPT>"}
         ]
       }],
       "generationConfig": {
         "responseModalities": ["IMAGE"],
         "imageConfig": {
           "aspectRatio": "<ASPECT_RATIO>"
         }
       }
     }' | jq -r '.candidates[0].content.parts[0].inlineData.data' | base64 -d > images/<FILENAME>.png
   ```

   - Default aspect ratio is `16:9` if not specified.
   - If the `jq` extraction fails or the file is empty, check the raw API response for error messages.

3. **Convert to optimised JPG** using sips (quality 60 hits ~200KB target from a single PNG source):
   ```bash
   sips -s format jpeg -s formatOptions 60 images/<FILENAME>.png --out images/<FILENAME>.jpg
   ```
   Do NOT re-compress an existing JPG — always convert from the PNG source to avoid double-compression artifacts.

4. **Verify the result:**
   - Read the generated JPG to visually inspect it.
   - Check file size — target is under 200KB. If over, regenerate from PNG at quality 50. If under 100KB, try quality 70.

5. **Clean up** the intermediate PNG:
   ```bash
   rm images/<FILENAME>.png
   ```

6. **Report** the result to the user: show the image and file size.

## Error Handling

- If the API returns an error about safety filters, try rephrasing the prompt to be less specific about people/faces.
- If the response JSON has no `candidates`, print the full response for debugging.
- Rate limit: ~500 requests/day on the free tier.

## Example

```
/generate-image "Professional photograph of a modern laboratory bench with scientific glassware" hero-science.jpg 16:9
```
