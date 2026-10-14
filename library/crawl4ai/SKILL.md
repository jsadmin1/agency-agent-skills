---
name: crawl4ai
description: Use an operator-configured, self-hosted Crawl4AI service for
  webpage-to-Markdown extraction, crawling, screenshots, PDFs, JavaScript page
  interaction and agent research retrieval. Trigger when the user asks to fetch
  a webpage cleanly, crawl or scrape a site, pull clean markdown from the
  internet, use Crawl4AI, or wire Crawl4AI into local LLM, app or harness
  workflows. Not for operating a hosted third-party scraping service or
  bypassing site access controls.
---
# Crawl4AI

Use the operator's self-hosted Crawl4AI service before falling back to ad hoc scraping for web extraction tasks. Crawl4AI is an open-source project (upstream: `github.com/unclecode/crawl4ai`); this skill covers using a running instance, not installing one.

## Service configuration

The operator supplies these; do not guess or hard-code them:

- Base URL: `CRAWL4AI_BASE_URL` (a local deployment commonly listens on `http://127.0.0.1:11235`; confirm the real value).
- MCP endpoints, if enabled: `CRAWL4AI_MCP_SSE_URL` and/or `CRAWL4AI_MCP_WS_URL`.
- Auth token: `CRAWL4AI_API_TOKEN`, already present in the environment of the process that needs it.
- Service root: the directory the operator uses to run and maintain the service, if they name one.

If the base URL or token is missing, stop and ask the operator to configure it. Never print, echo, log or paste the token, never read secret files to find it, and never ask the user to paste it into chat.

## Preferred use

Prefer a configured `crawl4ai` MCP server when available. Tools commonly exposed include:

- `md`: convert one webpage to clean Markdown
- `html`: return sanitized HTML
- `screenshot`: capture a rendered page screenshot
- `pdf`: capture a rendered page PDF
- `execute_js`: run constrained JavaScript on a page
- `crawl`: crawl one or more URLs
- `ask`: query Crawl4AI docs/context

Check the server's actual tool list rather than assuming these names.

For code or shell workflows, call the HTTP API with bearer auth from the existing environment. Keep shell tracing disabled and pass the header through stdin, not a process argument containing the token:

```bash
printf 'Authorization: Bearer %s\n' "$CRAWL4AI_API_TOKEN" | \
  curl -fsS --header @- \
  -H "Content-Type: application/json" \
  -d '{"url":"https://example.com","f":"fit"}' \
  "${CRAWL4AI_BASE_URL}/md"
```

Use `/md` for single-page clean Markdown and `/crawl` for multi-page or metadata-heavy extraction. Confirm endpoint names against the deployed version's API docs.

## Operational checks

Before debugging clients, verify the service itself: use the deployment's health endpoint or the operator's own health/test scripts in the service root, then one test fetch of `https://example.com`. Do not restart, reconfigure or expose the service without the operator's approval.

## Guardrails

- Keep the service bound to loopback unless the operator intentionally exposes it over a private network.
- Keep token auth enabled.
- Use constrained extraction/crawl requests before giving agents broad browser control.
- Avoid unbounded crawls. Set explicit URL lists, page limits or task-specific crawler config, and respect the target site's terms and robots rules.
- Do not commit environment files, tokens, logs, caches, screenshots, PDFs or scraped corpora unless they are intentionally public fixtures.
