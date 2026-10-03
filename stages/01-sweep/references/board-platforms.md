# Board platforms: platform by platform

How to read each kind of employer job board. The ground rules, location traps and signs a posting is gone are in `board-techniques.md`. Add what a session learns here (with the user's OK). Edit the platform's section in place. Never add employer names, the user's details or dates.

## Workday

The most common platform. Board addresses look like `<tenant>.wd<N>.myworkdayjobs.com/<site>` (some use `wd<N>.myworkdaysite.com/recruiting/<tenant>/<site>`).

- **List:** POST `/wday/cxs/<tenant>/<site>/jobs` with `{"appliedFacets":{},"limit":20,"offset":0,"searchText":""}`. It pages 20 at a time. On some boards `total` is returned only on the first page, so do not stop a loop when a later page reports 0.
- **Detail:** GET `/wday/cxs/<tenant>/<site>/job/<externalPath>`. Get `externalPath` from a search by job number. It already starts with `/job/`, so do not add `/job` again. Job paths can change when a title changes, so a 404 on a saved path is not proof the job is gone: search the job number first.
- **Same origin only.** The tab must be on that tenant's board.
- **Filter by location facets, not text.** POST with empty facets first, read the `facets` in the answer, then filter with the facet's own parameter name (often `locations`, sometimes a state or region facet, or `remoteType`). A text search for a state name also returns jobs that merely mention it.
  - A truly nationwide remote job usually carries every state's remote facet, so your state's remote facet catches it.
  - Some boards show only the top 50 or so facet values, so a small state may not appear; filter through the site's own search page instead. Some show no state facet until a country facet is applied first.
  - `searchText` is loose matching on some boards and cannot prove something does not exist.
- **Read `additionalLocations` on every job.** The list view does not show it, and real remote eligibility often lives there.
- **Liveness check without opening the form:** the detail endpoint returns `canApply`, `postedOn` and `endDate`. A 403 "permission denied" on the job endpoint, plus no match when searching the board for the job number, means the job is gone.
- If a job page shows only bare tags, inserting `/en-US/` after the host (`<host>/en-US/<site>/job/...`) often renders the full description.
- Some boards run a career site from another platform (Phenom and others) in front of Workday. The Workday feed underneath often works better.

## Phenom

- A plain fetch returns an empty shell. Use the rendered search page (`/global/en/search-results?keywords=<q>`) and its facet pages.
- **Feed:** POST `<careers host>/widgets` with `ddoKey` `"refineSearch"` (list) or `"jobDetail"` (detail); the payload needs the site's `refNum`. Results come back as an array of `{field, value}` items, not a keyed map.
- State filters differ by board: some want the two-letter code, some the full state name. Some state filters are simply broken; then filter on each row's own city and state.
- When `/widgets` returns 0 for everything, open a search URL and read `window.phApp.ddo.eagerLoadRefineSearch` from the page. Some boards cap that at the first 10 rows; then the board is manual for anything beyond a keyword search.
- On a job page, `document.body.innerText` may show only a chat widget. Read `phApp.ddo.jobDetail.data.job` instead.

## Greenhouse

- `boards-api.greenhouse.io/v1/boards/<token>/jobs?content=true` returns every posting with full text. Load `boards-api.greenhouse.io` in the tab first, then fetch.
- Find the token in the careers page's embed script: `boards.greenhouse.io/embed/job_board/js?for=<token>`, in the page's job links (`job-boards.greenhouse.io/<token>/jobs/<id>`), or in its network requests to `boards-api.greenhouse.io/v1/boards/<token>/`. Tokens are often not the company's obvious name.
- The same job number can be shared by copies of a job in several locations; log the job's own id.
- A `job-boards.greenhouse.io` job link that redirects to the employer's general careers page means the job is closed.
- Some boards turn over fast: a job can vanish between two reads minutes apart. Confirm twice before marking it gone.

## Ashby

`api.ashbyhq.com/posting-api/job-board/<slug>?includeCompensation=true` returns the whole board with plain-text descriptions, `isListed` and `publishedAt`. Fetch it from a tab on `api.ashbyhq.com`.

- The feed's `location` can be an office label such as "HQ" on a remote job. Read the posting's own "Location:" line in the description, and `secondaryLocations`, before judging place.

## Lever

`api.lever.co/v0/postings/<company>?mode=json` and `/<id>`. Includes `createdAt`, `salaryRange` and all locations. Load `api.lever.co` in the tab first.

## Workable

`apply.workable.com/api/v1/widget/accounts/<company>` lists jobs with their short codes.

## SmartRecruiters

`api.smartrecruiters.com/v1/companies/<id>/postings` and `/postings/<id>`. Employer front ends built on it may silently ignore their own location and keyword filters, so a filtered result of 0 means nothing there: page the whole board and filter the rows yourself.

## iCIMS

- Fetches fail unless the tab is already on that iCIMS host.
- Open `/jobs/<id>/job?in_iframe=1` and read the frame's `contentDocument`. Some pages set a base address, so use full same-origin addresses.
- The JSON-LD block's `datePosted` gives the posted date.
- Full lists often page with `pr=0..N` (20 per page). When the list sits inside a frame, fetch the frame address with `&in_iframe=1` and page it.
- Some boards ignore the country filter and return the global board: read each row's location.

## Jibe (a front end on iCIMS)

- GET `/api/jobs?page=N&limit=100`. The list already includes descriptions and qualifications, so one call can cover a board. Keep the page size modest: the result can be very large.
- `/api/jobs/<id>` returns HTML, so pull one job with `?keywords=<job number>&limit=5` instead.
- Work type can hide in a tag field. A location search may also return every nationwide posting, and on some boards the location sorts by distance instead of filtering.

## ADP Workforce Now

- The careers page embeds `<recruitment-current-openings cid="...">`.
- The public feed works even when the page never draws its list: `workforcenow.adp.com/mascsr/default/careercenter/public/events/staffing/v1/job-requisitions?cid=<cid>&lang=en_US&locale=en_US&$top=100`. **Each page holds at most 20 rows whatever `$top` says**, so page with `$skip`.
- `/job-requisitions/<itemID>?cid=<cid>` returns the description and pay range.
- When the board sits in a blank frame, find the cid in the careers page's HTML and call the feed directly.
- Try this before marking an ADP-hosted employer manual.

## ADP Career Center (myjobs.adp.com)

- `myjobs.adp.com/public/staffing/v1/career-site/<site name>` returns the site record (`orgoid`, the site `id`, and `settings.externalId`).
- The filter endpoint needs three lowercase headers sent together: `orgoid`, `postingchannelid` (the externalId) and `careersiteid` (the id). With all three it returns the board in one call.
- `job-requisitions?$top=N&$search=<term>` with an `orgoid` header also works; `$search` is the reliable filter because `$skip` stops working past several hundred rows.
- On job pages, `document.body.innerText` often returns only the footer. Read with `read_page` or `find`. A gone job shows a generic "Problem with the service" message: confirm with the board's own search.

## UKG Pro / UltiPro (recruiting.ultipro.com)

- POST `<board path>/JobBoardView/LoadSearchResults` with the search body the page uses.
- Detail: GET `<board path>/OpportunityDetail?opportunityId=<id>`. The HTML embeds `CandidateOpportunityDetail({...});` with description, posted date, locations, travel and pay range. Find the opening brace after the marker and match braces to the end, rather than relying on the closing parenthesis.
- A bare board address can 404 while the board's GUID address works. Take the GUID from the employer's careers-page link.
- A "System is initializing" page on first load is not a bot check: wait about 6 seconds and reload.

## UKG Ready (saashr.com)

Single-page boards with **no link per job**, so log postings by title. Take the tenant number (and any `ein_id`) from the employer's careers-page link. Some tenants expose a public feed at `/ta/rest/ui/recruitment/companies/%7C<tenant>/job-requisitions` and `/<id>` with full text.

## Dayforce

- GET `/api/auth/csrf`, then POST `/api/geo/<namespace>/jobposting/search` with header `x-csrf-token` and a body with `clientNamespace`, `cultureCode`, `jobBoardCode` (often `CANDIDATEPORTAL`), `searchText`, `paginationStart`. `searchText` matches the job number. The answer carries full descriptions, locations and posted time.
- On some boards the feed refuses scripted calls; the rendered page prints every description in full, so read that.

## Eightfold

- `/api/pcsx/search?domain=<domain>&query=...` returns positions. **`num` is silently capped at 10 on some boards** while `count` reports the real total: page with `start=`.
- Details: open `/careers/job/<id>?domain=<domain>` and wait about 2 seconds for it to fill in.
- On some boards a location search returns the nationwide remote board instead of local jobs; read each job's own location.

## Cornerstone (csod.com)

The careers site's own search calls `us.api.csod.com/rec-job-search/external/jobs`. Detail pages read fine as page text.

## Paycom

Next-page arrows can do nothing. Use the page's keyword box: set its value with the native input setter, dispatch an `input` event, then press Enter. A few broad words ("Sales", "Manager", "Associate") surface most titles. Reload between searches if the box stops taking a second query.

## Paylocity

- Board pages expose `window.pageData` with every job and its location.
- Detail at `/recruiting/jobs/Details/<id>`, which carries a JobPosting JSON-LD block. If that says "Job Not Found", the `/recruiting/jobs/Apply/<id>` address may work, and the tab must actually open it.
- No posted date and no pay range are exposed: that is the board's limit, not a gap in the read.
- A remote flag can be set on city jobs; prefer a location that says "Remote".

## Avature

- Location parameters in the address are often ignored.
- Some boards answer `GET /Search/SearchResults?keywords=&location=&jtStartIndex=N&jtPageSize=500` with header `X-Requested-With: XMLHttpRequest`. Values come wrapped in tags: strip them.
- Multi-state jobs can run state codes together in one string; look for your state's code as a separate token, and beware partial matches inside other words.
- Where that does not exist, type in the page's own location box and watch `read_network_requests` for the lookup it makes; reuse the ids it returns in the search address.

## Oracle Recruiting Cloud

- The site's REST feed: `recruitingCEJobRequisitions` with `finder=findReqs;siteNumber=<site>` for the list, and `recruitingCEJobRequisitionDetails` with `finder=ById;Id=<id>,siteNumber=<site>` for detail. The parameter is `Id`, not `jobId`. Find the host and site number with `performance.getEntriesByType('resource')` if the careers page hides them.
- When the feed is dead, click "Show more results" repeatedly on the rendered page and read the list.

## SuccessFactors

- Read the rendered career-site search, with job ids in the addresses.
- On some boards the tile search returns an empty 16-byte page for every query: that is not "no jobs". Try a `facetFilters` search on the site's own domain.
- On some boards the location search is broken while keyword search works.
- A keyword search for a job number may fall back to loose matching: check the exact job number is in the results before calling a job live.
- Some boards tag every job with the same work-type boilerplate; trust the body.
- Some careers hosts do not load in an automated browser while an alternate host for the same board does. Look for it on the employer's careers page.

## Other platforms

- **Radancy / TalentBrew:** `/search-jobs/results` with `RecordsPerPage=100` returns postings and facets. The location filter often returns the global board: use keywords and read each row's city. A keyword search on a bare job number returns exactly that job.
- **LiquidCompass:** the search feed ignores keyword and size parameters except `page_size`; pull the board whole and filter.
- **NLX / jobsyn:** the list caps at 10 rows; use `/sitemap.xml` and the jobs sitemap, where each job address starts with its city.
- **Hirebridge:** `recruit.hirebridge.com/v3/Jobs/list.aspx?cid=<cid>` and `JobDetails.aspx?cid=<cid>&jid=<id>`. Read the `<article>` element, not the whole page text.
- **Jobvite:** `jobs.jobvite.com/<slug>/jobs`. Parse job links from `/search?p=N`; some list classes do not survive a plain fetch.
- **Largely and other script-only boards:** click "Load more" until every card shows, then read the cards.
- **TTC Portals, Frontline and similar small boards:** read the rendered list, then each posting.
- **BambooHR:** `/careers/list` and `/careers/<id>/detail` return JSON. `locationType` "1" means remote.
- **HRMDirect:** skip the frame and open the job-openings list page directly; a plain fetch of a job page works from the board's own origin.
- **isolved Hire:** a fetch returns a shell; open each posting.
- **HiBob:** `<company>.careers.hibob.com`, read through `/api/job-ad`.
- **WordPress job boards:** `/wp-json/wp/v2/jobs` lists postings; each job page's HTML carries the location.
- **Sitemaps:** when a board's filters do nothing, `/sitemap.xml` often lists every job address.
- **Static careers pages and PDFs:** small; read them. A careers address that 404s may have moved: find the link on the employer's home page.
