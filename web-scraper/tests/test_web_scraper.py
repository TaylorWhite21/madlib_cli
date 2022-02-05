from web_scraper.scraper import get_citations_needed_count, get_citations_needed_report

expected_text = '''Even 131,000 channels were not enough to search the sky in detail at a fast rate, so Suitcase SETI was followed in 1985 by Project "META", for "Megachannel Extra-Terrestrial Assay". The META spectrum analyzer had a capacity of 8.4 million channels and a channel resolution of 0.05 hertz. An important feature of META was its use of frequency Doppler shift to distinguish between signals of terrestrial and extraterrestrial origin. The project was led by Horowitz with the help of the Planetary Society, and was partly funded by movie maker Steven Spielberg. A second such effort, META II, was begun in Argentina in 1990, to search the southern sky. META II is still in operation, after an equipment upgrade in 1996.[citation needed]
While most SETI sky searches have studied the radio spectrum, some SETI researchers have considered the possibility that alien civilizations might be using powerful lasers for interstellar communications at optical wavelengths. The idea was first suggested by R. N. Schwartz and Charles Hard Townes in a 1961 paper published in the journal Nature titled "Interstellar and Interplanetary Communication by Optical Masers". However, the 1971 Cyclops study discounted the possibility of optical SETI, reasoning that construction of a laser system that could outshine the bright central star of a remote star system would be too difficult. In 1983, Townes published a detailed study of the idea in the United States journal Proceedings of the National Academy of Sciences,[69] which was met with widespread agreement by the SETI community.[citation needed]
There are two problems with optical SETI.[citation needed] The first problem is that lasers are highly "monochromatic", that is, they emit light only on one frequency, making it troublesome to figure out what frequency to look for. However, emitting light in narrow pulses results in a broad spectrum of emission; the spread in frequency becomes higher as the pulse width becomes narrower, making it easier to detect an emission.
'''



def test_get_citations_needed_count():
    actual = get_citations_needed_count('https://en.wikipedia.org/wiki/Search_for_extraterrestrial_intelligence')
    expected = 3
    assert actual == expected

def test_get_citations_needed_report_first_line():
    actual = get_citations_needed_report('https://en.wikipedia.org/wiki/Search_for_extraterrestrial_intelligence')
    expected = expected_text
    assert actual == expected
