## blue-feed-red-feed-sources

These are the sources for Jon Keegan's "Blue Feed, Red Feed" Facebook project as published by the Wall Street Journal:
http://graphics.wsj.com/blue-feed-red-feed/

Per Keegan's original repository:
> This is a subset of data derived from Facebook's study: Bakshy, Eytan; Messing, Solomon; Adamic, Lada, 2015, “Replication Data for: Exposure to Ideologically Diverse News and Opinion on Facebook”, http://dx.doi.org/10.7910/DVN/LDJ7MS, Harvard Dataverse, V2

> We only included sources with `l2` and `r2` scores of .5 and above. We also only included sources with 100,000 or more "likes" (followers) as of the date of publish (May, 18, 2016). We removed some inactive sources, as well as broad ones like Wikipedia, Twitter and YouTube.

### Sampled Data

As a part of the simulation for our project, we have used Pandas to perform a simple random sample (SRS) of 30 sources of both "right" and "left" sources from Keegan's initial list. These samples are available in the `data/` folder.

### Site alignment

The following is directly quoted from the `README.md` of the Harvard study cited above:

>  The results in this paper rely on data that characterize URLs based on the
  the characteristics of individuals who share them.  We call this measure "alignment".
  We compute this measure by first mapping the 500 most common ideological affiliations
  listed in individuals' profile under the field "political views" to a five-point
  {-2, -1, 0, 1, 2} numerical representation.
  Then, for each "hard content" URL (see [1]), we compute the mean affiliation of
  every U.S. user over 18 who shared that URL who self-reports an affiliation
  that can be mapped onto the five-point scale.  This table summarizes the
  alignment of URLs for the top 500 most shared domains.

>  - `domain`: domain
>  - `avg_alignment`: Average alignment
>  - `l2`: proportion of shares with very liberal alignment from `domain`
>  - `l1`: proportion of shares with liberal alignment from `domain`
>  - `m`: proportion of shares with moderate alignment from `domain`
>  - `r1`: proportion of shares with conservative alignment from `domain`
>  - `r2`: proportion of shares with very conservative alignment from `domain`

>  The top 500 most shared domains have each been shared at least 44,000 times.
  This set of domains covers over 80% of the URLs classified as hard content that
  had been shared by individuals who self-report a political affiliation.
  All columns are rounded to the first 4 significant digits. Rows are ordered
  alphabetically.

>  Note that alignment is not a measure of slant or bias, it only characterizes
  the audience who shares a URL on Facebook. The measure may capture differences that include topic matter relevance, framing, etc., in addition to any "bias" present.
  Our intent here is not to characterize media bias, but instead to characterize the
  kind of content that partisans find important enough to share.  


  ### Updates

  - The like counts (`fan_count`) for the CSVs contained in the `data/` folder were recorded on March 26, 2018.
  - Since Keegan's initial data set, the Facebook IDs for "The Fox Nation" and "TakePart.com" had changed, and were updated on March 26, 2018.
