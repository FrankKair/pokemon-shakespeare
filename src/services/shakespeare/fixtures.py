from .models import Translation, Success, Contents


description_charizard = "CHARIZARD flies around the sky in\nsearch of powerful opponents.\nIt breathes fire of such great heat\fthat it melts anything. However, it\nnever turns its fiery breath on any\nopponent weaker than itself."


shakespeare_charizard = {
    'success': {
        'total': 1
    },
    'contents': {
        'translated': "Charizard flies 'round the sky in search of powerful opponents. 't breathes fire of such most wondrous heat yond 't melts aught. However,  't nev'r turns its fiery breath on any opponent weaker than itself.",
        'text': 'CHARIZARD flies around the sky in\nsearch of powerful opponents.\nIt breathes fire of such great heat\x0cthat it melts anything. However, it\nnever turns its fiery breath on any\nopponent weaker than itself.',
        'translation': 'shakespeare'
    }
}


translation_charizard = Translation(
    success=Success(total=1),
    contents=Contents(
        translated="Charizard flies 'round the sky in search of powerful opponents. 't breathes fire of such most wondrous heat yond 't melts aught. However,  't nev'r turns its fiery breath on any opponent weaker than itself.",
        text='CHARIZARD flies around the sky in\nsearch of powerful opponents.\nIt breathes fire of such great heat\x0cthat it melts anything. However, it\nnever turns its fiery breath on any\nopponent weaker than itself.',
        translation='shakespeare'
    )
)
