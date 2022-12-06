from apis.arxiv_api import Arxiv
from apis.acm_api import ACM
from apis.semantic_s import Semantic_Scholar

ap = Arxiv()
arxiv_result = ap.arxiv('Zero-shot learning', max_pages = 1)
print(arxiv_result.head(2))

# from apis.cnnp import connected_papers
#
# cp     = connected_papers()
# papers = cp.download_papers('Zero-shot learning', n=1)
# print(papers)

ac = ACM()
acm_result   = ac.acm('Zero-shot learning', max_pages = 1)
print(acm_result.head(2))


sc = Semantic_Scholar()
sc_result    = sc.ss('Zero-shot learning', max_pages = 1)
print(sc_result.head(2))
