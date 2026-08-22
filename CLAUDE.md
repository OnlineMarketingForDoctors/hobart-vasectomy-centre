# Hobart Vasectomy Centre

## NON-NEGOTIABLE: this site must not be indexed by search engines

This site is to be kept out of all search engine indexes. Treat this as a hard
requirement on every change until it is explicitly lifted by the site owner.

Every page, template, and layout MUST carry all of the following:

1. **Meta tag** — in the `<head>` of every HTML document:
   ```html
   <meta name="robots" content="noindex, nofollow, noarchive, nosnippet, noimageindex">
   ```
2. **HTTP header** — on every response, including non-HTML assets (PDF, images,
   JSON, RSS) which have no `<head>` to put a meta tag in:
   ```
   X-Robots-Tag: noindex, nofollow, noarchive, nosnippet, noimageindex
   ```
3. **robots.txt** — must ALLOW crawling. Do NOT use `Disallow: /`.
   A crawler that is blocked from fetching a page cannot read the `noindex`
   directive on it, and the URL can still be indexed title-only from inbound
   links. Blocking crawl actively defeats de-indexing.

### Also required

- No `sitemap.xml`, and no sitemap reference in `robots.txt`.
- Do not add Google Search Console verification, IndexNow, or any other
  submission/ping mechanism.
- No canonical tags pointing at this site from anywhere public.

### Checklist before any deploy

- [ ] Every route returns the `X-Robots-Tag` header
- [ ] Every rendered page contains the robots meta tag
- [ ] `robots.txt` does not contain `Disallow: /`
- [ ] No `sitemap.xml` is being served

Verify with:
```sh
curl -sI https://<host>/ | grep -i x-robots-tag
curl -s  https://<host>/ | grep -i 'name="robots"'
curl -s  https://<host>/robots.txt
```
