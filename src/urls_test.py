#! /usr/bin/python
# -*- coding: utf-8 -*-

"""Test urls.py module."""


import unittest

from src import dummy_requests
from src import urls
from src.urls import urls_sfn_cit_ref


class BostonTest(unittest.TestCase):

    def test_bg1(self):
        """boston.com, dateformat '%B %d, %Y'"""
        self.assertIn(
            '* {{cite web '
            '| last=Griffith '
            '| first=Bill '
            '| title=Hot Rod Stamps; Google on Road; A GM Prospectus '
            '| website=Boston.com '
            '| date=June 29, 2014 '
            '| url=https://www.boston.com/cars/news-and-reviews/2014/06/29/'
            'hot-rod-stamps-google-on-road-a-gm-prospectus '
            '| ref=harv '
            '| access-date=',
            urls_sfn_cit_ref(
                'http://www.boston.com/cars/news-and-reviews/2014/06/28/'
                'hot-rod-stamps-google-road-prospectus/hylbVi9qonAwBIH10CwiDP/'
                'story.html',
                '%B %d, %Y',
            )[1]
        )

    def test_bg2(self):
        """bostonglobe.com"""
        i = (
            'http://www.bostonglobe.com/metro/2014/06/03/'
            'walsh-meets-with-college-leaders-off-campus-housing/'
            'lsxtLSGJMD86Gbkjay3D6J/story.html'
        )
        o = urls_sfn_cit_ref(i)
        ct = (
            '* {{cite web '
            '| last=Saltzman '
            '| first=Jonathan '
            '| last2=Farragher '
            '| first2=Thomas '
            '| title=Walsh meets with college leaders on off-campus housing '
            '| website=BostonGlobe.com '
            '| date=2014-06-03 '
            '| url=https://www.bostonglobe.com/metro/2014/06/03/'
            'walsh-meets-with-college-leaders-off-campus-housing/'
            'lsxtLSGJMD86Gbkjay3D6J/story.html '
            '| ref=harv '
            '| access-date='
        )
        self.assertIn(ct, o[1])

    def test_bg3(self):
        """bostonmagazine.com. Author tags return unrelated authors."""
        i = (
            'http://www.bostonmagazine.com/news/blog/2013/08/21/'
            'juliette-kayyem-jumps-in-for-guv/'
        )
        o = urls_sfn_cit_ref(i)
        ct = (
            '* {{cite web '
            '| last=Bernstein '
            '| first=David S. '
            '| title=Juliette Kayyem Is Running for Governor of Massachusetts '
            '| website=Boston Magazine '
            '| date=2013-08-21 '
            '| url=http://www.bostonmagazine.com/news/blog/2013/08/21/'
            'juliette-kayyem-jumps-in-for-guv/ '
            '| ref=harv '
            '| access-date='
        )
        self.assertIn(ct, o[1])


class WashingtonpostTest(unittest.TestCase):

    def test_wp1(self):
        """`1 author, 2005, the pubdate is different from last edit date"""
        o = urls_sfn_cit_ref(
            'http://www.washingtonpost.com/wp-dyn/content/article/2005/09/02/'
            'AR2005090200822.html'
        )
        self.assertIn('{{sfn | Sachs | 2005}}', o[0])
        self.assertIn(
            '* {{cite web '
            '| last=Sachs '
            '| first=Andrea '
            '| title=March of the Migration '
            '| website=Washington Post '
            '| date=2005-09-04 '
            '| url=http://www.washingtonpost.com/wp-dyn/content/article/'
            '2005/09/02/AR2005090200822.html '
            '| ref=harv '
            '| access-date=',
            o[1],
        )


class HuffingtonpostTest(unittest.TestCase):

    def test_hp1(self):
        """`1 author, 2013"""
        o = urls_sfn_cit_ref(
            'http://www.huffingtonpost.ca/annelise-sorg/'
            'blackfish-killer-whale-seaworld_b_3686306.html'
        )
        self.assertIn('{{sfn | Sorg | 2013}}', o[0])
        self.assertIn(
            '* {{cite web '
            '| last=Sorg '
            '| first=Annelise '
            '| title=When Killer Whales Kill: Why the movie'
            ' "Blackfish" Should Sink Captive Whale Programs '
            '| website=The Huffington Post '
            '| date=2013-08-01 '
            '| url=http://www.huffingtonpost.ca/annelise-sorg/'
            'blackfish-killer-whale-seaworld_b_3686306.html '
            '| ref=harv '
            '| access-date=',
            o[1],
        )

    def test_hp2(self):
        """`class:author` returns wrong result. Disallow `\n` in fullnames."""
        i = (
            'http://www.huffingtonpost.com/jeremy-rifkin/'
            'obamas-climate-change-plan_b_5427656.html'
        )
        o = urls_sfn_cit_ref(i)
        e1 = '{{sfn | Rifkin | 2014}}'
        e2 = (
            "* {{cite web "
            "| last=Rifkin "
            "| first=Jeremy "
            "| title=Beyond Obama's Plan: "
            "A New Economic Vision for Addressing Climate Change "
            "| website=The Huffington Post "
            "| date=2014-06-02 "
            "| url=http://www.huffingtonpost.com/jeremy-rifkin/"
            "obamas-climate-change-plan_b_5427656.html "
            "| ref=harv "
            "| access-date="
        )
        self.assertIn(e1, o[0])
        self.assertIn(e2, o[1])


class DilyTelegraphTest(unittest.TestCase):

    def test_dt1(self):
        """`1 author, 2005"""
        i = (
            'http://www.telegraph.co.uk/news/health/3334755/'
            'We-could-see-the-whales-eyes-mouth...-'
            'the-barnacles-on-its-back.html'
        )
        o = urls_sfn_cit_ref(i)
        e1 = '{{sfn | Fogle | 2005}}'
        e2 = (
            "* {{cite web "
            "| last=Fogle "
            "| first=Ben "
            "| title=We could see the whale's eyes, mouth... "
            "the barnacles on its back "
            "| website=Telegraph.co.uk "
            "| date=2005-12-22 "
            "| url=http://www.telegraph.co.uk/news/health/3334755/"
            "We-could-see-the-whales-eyes-mouth...-"
            "the-barnacles-on-its-back.html "
            "| ref=harv "
            "| access-date="
        )
        self.assertIn(e1, o[0])
        self.assertIn(e2, o[1])

    def test_dt2(self):
        """1 author, 2003"""
        i = (
            'http://www.telegraph.co.uk/news/science/science-news/3313298/'
            'Marine-collapse-linked-to-whale-decline.html'
        )
        o = urls_sfn_cit_ref(i)
        e1 = '{{sfn | Highfield | 2003}}'
        e2 = (
            "* {{cite web "
            "| last=Highfield "
            "| first=Roger "
            "| title=Marine 'collapse' linked to whale decline "
            "| website=Telegraph.co.uk "
            "| date=2003-09-29 "
            "| url=http://www.telegraph.co.uk/news/science/science-news/"
            "3313298/Marine-collapse-linked-to-whale-decline.html "
            "| ref=harv "
            "| access-date="
        )
        self.assertIn(e1, o[0])
        self.assertIn(e2, o[1])

    def test_dt3(self):
        """1 author, 2011"""
        i = (
            'http://www.telegraph.co.uk/news/8323909/'
            'The-sperm-whale-works-in-extraordinary-ways.html'
        )
        o = urls_sfn_cit_ref(i)
        e1 = '{{sfn | Whitehead | 2011}}'
        e2 = (
            "* {{cite web "
            "| last=Whitehead "
            "| first=Hal "
            "| title=The sperm whale works in extraordinary ways "
            "| website=Telegraph.co.uk "
            "| date=2011-02-15 "
            "| url=http://www.telegraph.co.uk/news/science/8323909/"
            "The-sperm-whale-works-in-extraordinary-ways.html "
            "| ref=harv "
            "| access-date="
        )
        self.assertIn(e1, o[0])
        self.assertIn(e2, o[1])


class DilyMailTest(unittest.TestCase):

    def test_dm1(self):
        """4 authors"""
        o = urls_sfn_cit_ref(
            'http://www.dailymail.co.uk/news/article-2633025/'
            'London-cleric-convicted-NYC-terrorism-trial.html'
        )
        self.assertIn(
            '{{sfn | Malm | Witheridge | Drury | Bates | 2014}}', o[0]
        )
        self.assertIn(
            '* {{cite web '
            '| last=Malm '
            '| first=Sara '
            '| last2=Witheridge '
            '| first2=Annette '
            '| last3=Drury '
            '| first3=Ian '
            '| last4=Bates '
            '| first4=Daniel '
            '| title=Abu Hamza found guilty in US court of helping'
            ' Al-Qaeda terrorists '
            '| website=Daily Mail Online '
            '| date=2014-05-19 '
            '| url=http://www.dailymail.co.uk/news/article-2633025/'
            'London-cleric-convicted-NYC-terrorism-trial.html '
            '| ref=harv '
            '| access-date=',
            o[1],
        )

    def test_dm2(self):
        """`for` in byline."""
        self.assertIn(
            '* {{cite web '
            '| last=Gower '
            '| first=Eleanor '
            "| title=Kim Kardashian's meltdown at nude magazine cover"
            " three years before full frontal photoshoot "
            '| website=Daily Mail Online '
            '| date=2014-11-14 '
            '| url=http://www.dailymail.co.uk/tvshowbiz/article-2834145/'
            'I-m-never-taking-clothes-s-Vogue-Throwback-2011-video-shows-Kim-'
            'Kardashian-s-meltdown-nude-magazine-cover.html '
            '| ref=harv '
            '| access-date=',
            urls_sfn_cit_ref(
                'http://www.dailymail.co.uk/tvshowbiz/article-2834145/'
                'I-m-never-taking-clothes-s-Vogue-Throwback-2011-video-'
                'shows-Kim-Kardashian-s-meltdown-nude-magazine-cover.html'
            )[1],
        )


class BbcTest(unittest.TestCase):

    def test_bbc1(self):
        """no authors"""
        i = 'https://www.bbc.com/news/world-asia-27653361'
        o = urls_sfn_cit_ref(i)
        ct = (
            "* {{cite web "
            "| title=US 'received Qatar assurances' on Afghan prisoner deal "
            "| website=BBC News "
            "| date=2014-06-01 "
            "| url=http://www.bbc.com/news/world-asia-27653361 "
            "| ref={{sfnref | BBC News | 2014}} "
            "| access-date="
        )
        self.assertIn(ct, o[1])

    def test_bbc2(self):
        """1 author"""
        self.assertIn(
            '* {{cite web '
            '| last=Gage '
            '| first=Suzi '
            '| title=Sea otter return boosts ailing seagrass in California '
            '| website=BBC News '
            '| date=2013-08-26 '
            '| url=http://www.bbc.com/news/science-environment-23814524 '
            '| ref=harv '
            '| access-date=',
            urls_sfn_cit_ref(
                'http://www.bbc.com/news/science-environment-23814524'
            )[1],
        )

    def test_bbc3(self):
        """https version of bbc2 (differs a lot!)"""
        i = 'https://www.bbc.com/news/science-environment-23814524'
        o = urls_sfn_cit_ref(i)
        ct = (
            '* {{cite web '
            '| last=Gage '
            '| first=Suzi '
            '| title=Sea otter return boosts ailing seagrass in California '
            '| website=BBC News '
            '| date=2013-08-26 '
            '| url=http://www.bbc.com/news/science-environment-23814524 '
            '| ref=harv '
            '| access-date='
        )
        self.assertIn(ct, o[1])

    def test_bbc4(self):
        """news.bbc.co.uk, 1 author"""
        self.assertIn(
            "* {{cite web "
            "| last=Jones "
            "| first=Meirion "
            "| title=Malaria advice 'risks lives' "
            "| website=BBC NEWS "
            "| date=2006-07-13 "
            "| url="
            "http://news.bbc.co.uk/2/hi/programmes/newsnight/5178122.stm "
            "| ref=harv "
            "| access-date=",
            urls_sfn_cit_ref(
                'http://news.bbc.co.uk/2/hi/programmes/newsnight/5178122.stm'
            )[1],
        )

    def test_bbc5(self):
        """news.bbc.co.uk, 1 author"""
        self.assertIn(
            "* {{cite web "
            "| last=Madslien "
            "| first=Jorn "
            "| title=Inside the Bentley factory "
            "| website=BBC NEWS "
            "| date=2002-12-24 "
            "| url=http://news.bbc.co.uk/2/hi/business/2570109.stm "
            "| ref=harv "
            "| access-date=",
            urls_sfn_cit_ref(
                'http://news.bbc.co.uk/2/hi/business/2570109.stm'
            )[1],
        )

    def test_bbc6(self):
        """bbc.com, 1 author"""
        i = 'http://www.bbc.com/news/science-environment-26267918'
        o = urls_sfn_cit_ref(i)
        ct = (
            "* {{cite web "
            "| last=Amos "
            "| first=Jonathan "
            "| title=European Space Agency picks Plato planet-hunting mission "
            "| website=BBC News "
            "| date=2014-02-20 "
            "| url=http://www.bbc.com/news/science-environment-26267918 "
            "| ref=harv "
            "| access-date="
        )
        self.assertIn(ct, o[1])

        
class NytTest(unittest.TestCase):

    def test_nyt1(self):
        """newstylct, 1 author"""
        i = (
            'http://www.nytimes.com/2014/05/30/business/international/'
            'on-the-internet-the-right-to-forget-vs-the-right-to-know.html?'
            'hp&_r=0'
        )
        o = urls_sfn_cit_ref(i)
        ct = (
            '* {{cite web '
            '| last=Hakim '
            '| first=Danny '
            '| title=Right to Be Forgotten? Not That Easy '
            '| website=The New York Times '
            '| date=2014-05-30 '
            '| url=https://www.nytimes.com/2014/05/30/business/international/'
            'on-the-internet-the-right-to-forget-vs-the-right-to-know.html '
            '| ref=harv '
            '| access-date='
        )
        self.assertIn(ct, o[1])

    def test_nyt2(self):
        """newstylct, 2 authors"""
        ct = (
            '* {{cite web '
            '| last=Belson '
            '| first=Ken '
            '| last2=Sandomir '
            '| first2=Richard '
            '| title=$2 Billion for Clippers? In Time, '
            'It May Be a Steal for Steve Ballmer '
            '| website=The New York Times '
            '| date=2014-05-30 '
            '| url=https://www.nytimes.com/2014/05/31/sports/basketball/'
            'steven-a-ballmers-2-billion-play-for-clippers-is-a-big-bet-on-'
            'the-nba.html '
            '| ref=harv '
            '| access-date='
        )
        self.assertIn(
            ct,
            urls_sfn_cit_ref(
                'https://www.nytimes.com/2014/05/31/sports/basketball/'
                'steven-a-ballmers-2-billion-play-for-clippers-is-a-big-bet-'
                'on-the-nba.html?hp'
            )[1],
        )

    def test_nyt3(self):
        """oldstylct, 1 author"""
        i = 'http://www.nytimes.com/2007/12/25/world/africa/25kenya.html'
        o = urls_sfn_cit_ref(i)
        ct = (
            '* {{cite web '
            '| last=Gettleman '
            '| first=Jeffrey '
            '| title=Election Rules Complicate Kenya Race '
            '| website=The New York Times '
            '| date=2007-12-25 '
            '| url=https://www.nytimes.com/2007/12/25/world/africa/'
            '25kenya.html '
            '| ref=harv '
            '| access-date='
        )
        self.assertIn(ct, o[1])

    def test_nyt4(self):
        """newstylct, 2 authors, only byline"""
        i = (
            'http://dealbook.nytimes.com/2014/05/30/'
            'insider-trading-inquiry-includes-mickelson-and-icahn/'
        )
        o = urls_sfn_cit_ref(i)
        ct = (
            '* {{cite web '
            '| last=Goldstein '
            '| first=Matthew '
            '| last2=Protess '
            '| first2=Ben '
            '| title=Investor, Bettor, Golfer: '
            'Insider Trading Inquiry Includes Mickelson, Icahn and William T. '
            'Walters '
            '| website=DealBook '
            '| date=2014-06-12 '
            '| url=https://dealbook.nytimes.com/2014/05/30/'
            'insider-trading-inquiry-includes-mickelson-and-icahn/ '
            '| ref=harv '
            '| access-date='
        )
        self.assertIn(ct, o[1])

    def test_nyt5(self):
        """special case for date format (not in usual meta tags)"""
        i = (
            'https://www.nytimes.com/2007/06/13/world/americas/'
            '13iht-whale.1.6123654.html'
        )
        o = urls_sfn_cit_ref(i)
        ct = (
            '* {{cite web '
            '| title=19th-century harpoon gives clue on whales '
            '| website=The New York Times '
            '| date=2007-06-13 '
            '| url=https://www.nytimes.com/2007/06/13/world/americas/'
            '13iht-whale.1.6123654.html '
            '| ref={{sfnref | The New York Times | 2007}} '
            '| access-date='
        )
        self.assertIn(ct, o[1])

    def test_nyt6(self):
        """lastname=O'Connor"""
        i = (
            'http://www.nytimes.com/2003/10/09/us/'
            'adding-weight-to-suspicion-sonar-is-linked-to-whale-deaths.html'
        )
        o = urls_sfn_cit_ref(i)
        ct = (
            "* {{cite web "
            "| last=O'Connor "
            "| first=Anahad "
            "| title=Adding Weight to Suspicion, "
            "Sonar Is Linked to Whale Deaths "
            "| website=The New York Times "
            "| date=2003-10-09 "
            "| url=https://www.nytimes.com/2003/10/09/us/"
            "adding-weight-to-suspicion-sonar-is-linked-to-whale-deaths.html "
            "| ref=harv "
            "| access-date="
        )
        self.assertIn(ct, o[1])
        

class TGDaily(unittest.TestCase):

    def test_tgd2(self):
        """Hard to find author and date."""
        i = (
            'http://www.tgdaily.com/web/'
            '100381-apple-might-buy-beats-for-32-billion'
        )
        o = urls_sfn_cit_ref(i)
        ct = (
            '* {{cite web '
            '| title=Apple might buy Beats for $3.2 billion '
            '| website=TG Daily '
            '| date=2014-05-09 '
            '| url=http://www.tgdaily.com/web/'
            '100381-apple-might-buy-beats-for-32-billion '
            '| ref={{sfnref | TG Daily | 2014}} '
            '| access-date='
        )
        self.assertIn(ct, o[1])

    def test_tgd3(self):
        """"Staff" in author name."""
        i = (
            'http://www.tgdaily.com/space-features/'
            '82906-sma-reveals-giant-star-cluster-in-the-making'
        )
        o = urls_sfn_cit_ref(i)
        ct = (
            '* {{cite web '
            '| title=SMA reveals giant star cluster in the making '
            '| website=TG Daily '
            '| date=2013-12-17 '
            '| url=http://www.tgdaily.com/space-features/'
            '82906-sma-reveals-giant-star-cluster-in-the-making '
            '| ref={{sfnref | TG Daily | 2013}} '
            '| access-date='
        )
        self.assertIn(ct, o[1])


@unittest.skip
class NotWorking(unittest.TestCase):
    def test_tgd1(self):
        """ABCNews. Wrong author:  | last=News | first=ABC."""
        i = 'http://abcnews.go.com/blogs/headlines/2006/12/saddam_executed/'
        o = urls_sfn_cit_ref(i)
        ct = (
            '* {{cite web '
            '| last=Ross '
            '| first=Brian '
            '| title=Saddam Executed; An Era Comes to an End '
            '| website=ABC News Blogs '
            '| date=2006-12-30 '
            '| url=http://abcnews.go.com/blogs/headlines/2006/12/'
            'saddam_executed/ '
            '| ref=harv '
            '| access-date='
        )
        self.assertIn(ct, o[1])

    def test_oth12(self):
        """Times of India, author could not be detected."""
        i = (
            'http://timesofindia.indiatimes.com/city/pune/'
            'UK-allows-working-visas-for-Indian-students/'
            'articleshow/1163528927.cms?'
        )
        o = urls_sfn_cit_ref(i)
        sfn = "{{sfn | Kashyap | 2001}}"
        self.assertIn(sfn, o[0])


class Others(unittest.TestCase):

    def test_oth1(self):
        """Get title by hometitle comparison."""
        i = 'http://www.ensani.ir/fa/content/326173/default.aspx'
        o = urls_sfn_cit_ref(i)
        ct = (
            '* {{cite web '
            '| last=جلیلیان '
            '| first=شهرام '
            '| last2=نیا '
            '| first2=امیر علی '
            '| title=ورود کاسی ها به میان رودان و پیامدهای آن '
            '| website=پرتال جامع علوم انسانی '
            '| date=2014-05-20 '
            '| url=http://www.ensani.ir/fa/content/326173/default.aspx '
            '| language=fa '
            '| ref=harv '
            '| access-date='
        )
        self.assertIn(ct, o[1])

    def test_text_search(self):
        """Match byline on soup.text."""
        self.assertIn(
            '* {{cite web '
            '| last=Carlson '
            '| first=Kimberly '
            '| last2=York '
            '| first2=Jillian C. '
            '| title=Sudan Tech Sanctions Harm Innovation and Development: '
            'US Government and Corporations Must Act '
            '| website=Electronic Frontier Foundation '
            '| date=2014-06-26 '
            '| url=https://www.eff.org/deeplinks/2014/06/'
            'sudan-tech-sanctions-harm-innovation-development-us-'
            'government-and-corporations-must-act '
            '| ref=harv '
            '| access-date=',
            urls_sfn_cit_ref(
                'https://www.eff.org/deeplinks/2014/06/'
                'sudan-tech-sanctions-harm-innovation-development-us-'
                'government-and-corporations-must-act'
            )[1],
        )

    # Disable because relies on class="author" which has been disabled due
    # to hight error rate.
    @unittest.skip
    def test_oth3(self):
        """4 authors."""
        i = (
            'https://arstechnica.com/science/2007/09/'
            'the-pseudoscience-behind-homeopathy/'
        )
        o = urls_sfn_cit_ref(i)
        ct = (
            '* {{cite web '
            '| last=Timmer '
            '| first=John '
            '| last2=Ford '
            '| first2=Matt '
            '| last3=Lee '
            '| first3=Chris '
            '| last4=Gitlin '
            '| first4=Jonathan '
            '| title=Diluting the scientific method:  Ars looks at homeopathy '
            '| website=Ars Technica '
            '| date=2007-09-12 '
            '| url=https://arstechnica.com/science/2007/09/'
            'the-pseudoscience-behind-homeopathy/ '
            '| ref=harv '
            '| access-date='
        )
        self.assertIn(ct, o[1])

    def test_oth4(self):
        """rel="author" tag contains invalid information."""
        self.assertIn(
            "* {{cite web "
            "| last=Ghose "
            "| first=Tia "
            "| title='Revolutionary' Physics:"
            " Do Sterile Neutrinos Lurk in the Universe? "
            "| website=Live Science "
            "| date=2014-07-01 "
            "| url=http://www.livescience.com/"
            "46619-sterile-neutrino-experiment-beginning.html "
            "| ref=harv "
            "| access-date=",
            urls_sfn_cit_ref(
                'http://www.livescience.com/'
                '46619-sterile-neutrino-experiment-beginning.html?'
                'cmpid=514645_20140702_27078936'
            )[1],
        )

    def test_oth5(self):
        """Getting the date is tricky here."""
        o = urls_sfn_cit_ref('http://www.magiran.com/npview.asp?ID=1410487')
        self.assertIn('{{sfn | نوري | 2007}}', o[0])
        self.assertIn(
            '* {{cite web '
            '| last=نوري '
            '| first=آزاده شهمير '
            '| title=روزنامه سرمايه86/3/1: دكتر طاهر صباحي، محقق و مجموعه دار'
            ' فرش: بازار جهاني با توليد فرش هنري نصيب ايران مي شود '
            '| website=magiran.com '
            '| date=2007-05-22 '
            '| url=http://www.magiran.com/npview.asp?ID=1410487 '
            '| language=fa '
            '| ref=harv '
            '| access-date=',
            o[1],
        )

    def test_oth6(self):
        """Detection of website name."""
        o = urls_sfn_cit_ref(
            'http://www.farsnews.com/newstext.php?nn=13930418000036'
        )
        self.assertIn("{{sfn | ''خبرگزاری فارس'' | 2014}}", o[0])
        # Fars news is using 'خبرگزاری فارس' as og:author which is wrong
        # and thats why its name is not italicized in sfn.
        self.assertIn(
            '* {{cite web '
            '| title=آیت\u200cالله محمدی گیلانی دارفانی را وداع گفت '
            '| website=خبرگزاری فارس '
            '| date=2014-07-09 '
            '| url=http://www.farsnews.com/newstext.php?nn=13930418000036 '
            '| language=fa '
            '| ref={{sfnref | خبرگزاری فارس | 2014}} '
            '| access-date=',
            o[1],
        )

    def test_oth7(self):
        """Contains a By Topic line and also the byline contains ' | '."""
        self.assertIn(
            '* {{cite web '
            '| last=Chandler '
            '| first=David L. '
            '| title=Traffic lights: There’s a better way '
            '| website=MIT News '
            '| date=2014-07-07 '
            '| url=http://news.mit.edu/2014/'
            'traffic-lights-theres-a-better-way-0707 '
            '| ref=harv '
            '| access-date=',
            urls_sfn_cit_ref(
                'http://news.mit.edu/2014/'
                'traffic-lights-theres-a-better-way-0707'
            )[1],
        )

    def test_oth8(self):
        """Two authors from guardian that are mentions in other tags, too."""
        i = (
            'http://www.theguardian.com/world/2014/jul/14/'
            'israel-drone-launched-gaza-ashdod'
        )
        o = urls_sfn_cit_ref(i)
        ct = (
            '* {{cite web '
            '| last=Beaumont '
            '| first=Peter '
            '| last2=Crowcroft '
            '| first2=Orlando '
            '| title=Israel says it has shot down drone launched from Gaza '
            '| website=the Guardian '
            '| date=2014-07-14 '
            '| url=http://www.theguardian.com/world/2014/jul/14/'
            'israel-drone-launched-gaza-ashdod '
            '| ref=harv '
            '| access-date='
        )
        self.assertIn(ct, o[1])

    def test_oth10(self):
        """The Times. (Authors found by "byline" css selector)"""
        self.assertIn(
            '* {{cite web '
            '| last=Lagan '
            '| first=Bernard '
            '| last2=Charter '
            '| first2=David '
            '| title='
            'Woman who lost brother on MH370 mourns relatives on board MH17 '
            '| website=The Times & The Sunday Times '
            '| date=2014-07-18 '
            '| url=https://www.thetimes.co.uk/article/'
            'woman-who-lost-brother-on-mh370-mourns-relatives-on-board-'
            'mh17-r07q5rwppl0 '
            '| ref=harv '
            '| access-date=',
            urls_sfn_cit_ref(
                'http://www.thetimes.co.uk/tto/news/world/'
                'australia-newzealand/article4151214.ece'
            )[1]
        )

    def test_oth11(self):
        """Business News Daily."""
        i = (
            'http://www.businessnewsdaily.com/6762-male-female-entrepreneurs'
            '.html?cmpid=514642_20140715_27858876'
        )
        o = urls_sfn_cit_ref(i)
        ct = (
            '* {{cite web '
            '| last=Helmrich '
            '| first=Brittney '
            '| title=Male vs. Female Entrepreneurs: How Are They Different? '
            '| website=Business News Daily '
            '| date=2014-07-10 '
            '| url=http://www.businessnewsdaily.com/6762-male-female-'
            'entrepreneurs.html '
            '| ref=harv '
            '| access-date='
        )
        self.assertIn(ct, o[1])

    def test_oth12(self):
        """thebulletin.org"""
        i = 'http://thebulletin.org/evidence-shows-iron-dome-not-working7318'
        o = urls_sfn_cit_ref(i)
        ct = (
            '* {{cite web '
            '| last=Postol '
            '| first=Theodore A. '
            '| title=The evidence that shows Iron Dome is not working '
            '| website=Bulletin of the Atomic Scientists '
            '| date=2014-07-19 '
            '| url=http://thebulletin.org/'
            'evidence-shows-iron-dome-not-working7318 '
            '| ref=harv '
            '| access-date='
        )
        self.assertIn(ct, o[1])

    def test_reverse_name(self):
        """Author is `Martin, Tracy`. Tracy should be the first name."""
        self.assertIn(
            '* {{cite web '
            '| last=Martin '
            '| first=Tracy '
            '| title=Dynamometers Explained '
            '| website=HighBeam Research '
            '| date=2014-07-01 '
            '| url=http://www.highbeam.com/doc/1P3-3372742961.html '
            '| ref=harv '
            '| access-date=',
            urls_sfn_cit_ref(
                'http://www.highbeam.com/doc/1P3-3372742961.html'
            )[1],
        )

    def test_oth14(self):
        """thebulletin.org"""
        i = (
            'http://www.independent.co.uk/news/business/'
            'the-investment-column-tt-group-1103208.html'
        )
        o = urls_sfn_cit_ref(i)
        ct = (
            '* {{cite web '
            '| title=The Investment column: TT Group '
            '| website=The Independent '
            '| date=1999-06-29 '
            '| url=http://www.independent.co.uk/news/business/'
            'the-investment-column-tt-group-1103208.html '
            '| ref={{sfnref | The Independent | 1999}} '
            '| access-date='
        )
        self.assertIn(ct, o[1])

    def test_oth15(self):
        """Contains <link property="og:site_name" href="ایسنا" />"""
        self.assertIn(
            '* {{cite web '
            '| title=برجام شرایط بین‌المللی ایران را کاملا متحول کرد '
            '| website=ایسنا '
            '| date=2017-01-25 '
            '| url=http://www.isna.ir/news/95110603890/ '
            '| language=fa '
            '| ref={{sfnref | ایسنا | 2017}} '
            '| access-date=',
            urls_sfn_cit_ref(
                'http://www.isna.ir/news/95110603890/'
                '%D8%A8%D8%B1%D8%AC%D8%A7%D9%85-%D8%B4%D8%B1%D8%A7%DB%8C%D8%B7'
                '-%D8%A8%DB%8C%D9%86-%D8%A7%D9%84%D9%85%D9%84%D9%84%DB%8C-'
                '%D8%A7%DB%8C%D8%B1%D8%A7%D9%86-%D8%B1%D8%A7-'
                '%DA%A9%D8%A7%D9%85%D9%84%D8%A7-%D9%85%D8%AA%D8%AD%D9%88%D9%84'
                '-%DA%A9%D8%B1%D8%AF'
            )[1],
        )

    def test_invalid_name(self):
        """Test that URL does not fail with InvalidNameError."""
        self.assertIn(
            '* {{cite web | title=انتخابات 96 به روایت آمار '
            '| website=پایگاه اطلاع رسانی شبکه خبر صدا'
            ' و سیمای جمهوری اسلامی ایران |'
            ' date=2017-05-24 | url=http://www.irinn.ir/fa/news/499654 '
            '| language=fa | ref={{sfnref |'
            ' پایگاه اطلاع رسانی شبکه خبر'
            ' صدا و سیمای جمهوری اسلامی ایران | 2017}} |'
            ' access-date=',
            urls_sfn_cit_ref(
                'http://www.irinn.ir/fa/news/499654/'
                '%D8%A7%D9%86%D8%AA%D8%AE%D8%A7%D8%A8%D8%A7%D8%AA-96-'
                '%D8%A8%D9%87-%D8%B1%D9%88%D8%A7%DB%8C%D8%AA-'
                '%D8%A2%D9%85%D8%A7%D8%B1'
            )[1],
        )

    def test_pages_from_html_meta(self):
        """Test extracting pages from html meta tags."""
        self.assertIn(
            '* {{cite journal '
            '| last=جلیلیان '
            '| first=شهرام '
            '| title=نهاد دایگانی در دورۀ ساسانیان '
            '| journal=تحقیقات تاریخ اجتماعی '
            '| volume=2 '
            '| issue=1 '
            '| date=2012-09-17 '
            '| issn=2383-0484 '
            '| pages=53–74 '
            '| url=http://socialhistory.ihcs.ac.ir/article_319_84.html '
            '| language=fa '
            '| ref=harv '
            '| access-date=',
            urls_sfn_cit_ref(
                'http://socialhistory.ihcs.ac.ir/article_319_84.html'
            )[1],
        )

    def test_empty_meta_author_content(self):
        """Test that the output will not be malformed because empty meta."""
        self.assertIn(
            "* {{cite web "
            "| title=UAE's Enoc pays Iran $4 billion in oil dues "
            "| website=Al Jazeera "
            "| date=2017-05-29 "
            "| url=http://www.aljazeera.com/news/2017/05/uae-enoc-pays-iran-4-"
            "billion-oil-dues-170529171315570.html "
            "| ref={{sfnref | Al Jazeera | 2017}} "
            "| access-date=",
            urls_sfn_cit_ref(
                'http://www.aljazeera.com/news/2017/05/'
                'uae-enoc-pays-iran-4-billion-oil-dues-170529171315570.html'
            )[1],
        )

    def test_citation_author_reverse_order(self):
        """Test correct detection of citation_author.

        first name and last name are in reverse order.

        """
        self.assertIn(
            '* {{cite web '
            '| last=Hartman '
            '| first=JudithAnn R. '
            '| last2=Nelson '
            '| first2=Eric A. '
            '| title=Automaticity in Computation and Student Success in '
            'Introductory Physical Science Courses '
            '| website=arXiv.org e-Print archive '
            '| date=2016-08-17 '
            '| url=https://arxiv.org/abs/1608.05006?utm_medium=email&'
            'utm_source=other&utm_campaign=opencourse.GdeNrll1EeSROyIACtiVvg.'
            'announcements%257Eopencourse.GdeNrll1EeSROyIACtiVvg.'
            '4xDVKzx5EeeJjRJrkGD1dA '
            '| ref=harv '
            '| access-date=',
            urls_sfn_cit_ref(
                'https://arxiv.org/abs/1608.05006?utm_medium=email&utm_source='
                'other&utm_campaign=opencourse.GdeNrll1EeSROyIACtiVvg.'
                'announcements%257Eopencourse.GdeNrll1EeSROyIACtiVvg.'
                '4xDVKzx5EeeJjRJrkGD1dA'
            )[1],
        )

    def test_single_line_meta_tags(self):
        """Issue #9."""
        self.assertIn(
            "* {{cite web | last=Shoichet | first=Catherine E. "
            "| title=Spill spews tons of coal ash into North Carolina's "
            "Dan River | website=CNN | date=2014-02-09 "
            "| url=http://www.cnn.com/2014/02/09/us/north-carolina-coal-ash"
            "-spill/index.html | ref=harv | access-date=",
            urls_sfn_cit_ref(
                'https://edition.cnn.com/'
                '2014/02/09/us/north-carolina-coal-ash-spill/'
            )[1],
        )


dummy_requests = dummy_requests.DummyRequests()
urls.requests_get = dummy_requests.get
urls.requests_head = dummy_requests.head
if __name__ == '__main__':
    unittest.main()
