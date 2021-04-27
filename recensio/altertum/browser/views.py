from recensio.theme.browser.homepage import HomepageView
from recensio.theme.browser.pdfgen import GeneratePdfRecension


class GeneratePdfRecensionAltertum(GeneratePdfRecension):
    """Customized cover page"""

    logo_main = "++resource++recensio.altertum.images/logo2_fuer-Deckblatt.jpg"


class AltertumHomepageView(HomepageView):

    review_languages = [u""]
