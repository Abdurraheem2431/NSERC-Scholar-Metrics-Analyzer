from scholarly import scholarly

def getCounts(name,year):
    author_name = name
    author_year = year

   
    search_query = scholarly.search_author(author_name)

    try:
        author = next(search_query)
    except StopIteration:
        print("No authors found.")
        return (0, 0)

   
    author_data = scholarly.fill(author)

    publications = author_data['publications']
    publications_in_year = []
    citations_in_year = 0

    for pub in publications:
        pub_year = pub.get('bib', {}).get('pub_year')
        if pub_year and str(pub_year) == str(author_year):
            publications_in_year.append(pub)
            citations_in_year += pub.get('num_citations', 0)

    return len(publications_in_year), citations_in_year
