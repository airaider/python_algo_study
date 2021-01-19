import collections
import re


def solution(word, pages):

    word = word.lower()

    url_idx={}
    url_score={}
    url_href=collections.defaultdict(list)
    idx = 0

    for page in pages:
        page = page.lower()

        url = re.search(r'<meta[^>]*content="https://([\S]*)"/>',page).group(1)
        url_idx[url] = idx
        idx += 1

        link = re.findall('<a href=\"https://(.*?)\"',page)
        cnt=0
        for i in re.findall(r'[a-zA-Z]+', page):
            if i == word:
                cnt+=1

        url_score[url] = [cnt, link]
        for l in link:
            url_href[l].append(url)

    result = []

    for k, v in url_score.items():
        score = 0
        for val in url_href[k]:
            score += (url_score[val][0]/len(url_score[val][1]))
        score += v[0]
        result.append([score, url_idx[k]])

    print(sorted(result, key=lambda x:[-x[0], x[1]])[0][1])
    return


if __name__ == '__main__':
    word = "blind"
    pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
    solution(word, pages)