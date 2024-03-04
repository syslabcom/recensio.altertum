from recensio.plone.browser.homepage import HomepageView
from recensio.plone.browser.pdfgen import GeneratePdfRecension


class GeneratePdfRecensionAltertum(GeneratePdfRecension):
    """Customized cover page"""

    logo_main = "++resource++recensio.altertum.images/logo2_fuer-Deckblatt.jpg"


class AltertumHomepageView(HomepageView):

    resource_directory = "++resource++recensio.altertum.images"
    review_languages = [""]
