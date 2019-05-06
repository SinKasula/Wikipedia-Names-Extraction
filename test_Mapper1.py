#!/usr/bin/env python
from __future__ import with_statement
from __future__ import absolute_import
import xml.etree.ElementTree as et
import re
from io import open
#from django.utils.encoding import smart_str, smart_unicode

path = u'enwiki-20181120-pages-articles-multistream.xml'
#data = open(path, encoding=u'UTF8')
#print type(data)

#with open(path, 'r', encoding=u"UTF8") as xml_file:
    #tree = et.parse(xml_file)
#    data = smart_str(xml_file.read())

parser = et.XMLParser(encoding='utf-8')
tree = et.parse( path, parser=parser )
#print tree
#tree = et.parse(data)
#tree_decoded = tree.encode('utf8', replace)
#tree = et.parse(data)
root = tree.getroot()
#print("herer")
#print root
#print(type(root))
list_titles = []
list_names = []
dict_redict = dict()


# returns true for bio-stub and people-stub
def filter_by_stub(rev):
    people_stub_tag = rev.text.lower().find(u'{{people-stub}}')
    bio_stub_tag = rev.text.lower().find(u'{{bio-stub}}')
    if (people_stub_tag != -1 or bio_stub_tag != -1):
        return True
    else:
        return False


# returns true carrer and life section
def filter_by_section(rev):
    early_life_1 = rev.text.lower().find(u'== early life')
    early_life_2 = rev.text.lower().find(u'==early life')

    if (early_life_1 != -1 or early_life_2 != -1):
        return True
    else:
        return False


# returns true for category people
def filter_by_category(rev):
    category_births_1 = re.search(u'\[\[category:[a-z A-Z 0-9]{1,20}births\]\]', rev.text.lower())
    category_deaths_1 = re.search(u'\[\[category:[a-z A-Z 0-9]{1,20}deaths\]\]', rev.text.lower())
    category_living_people = rev.text.lower().find(u'[[category:living people]]')
    if (category_births_1 is not None or category_living_people != -1 or category_deaths_1 is not None):
        return True
    else:
        return False


# returns true for category people
def filter_by_redirectIntext(rev):
    catRedirect1 = re.search(u'#REDIRECT\s{0,2}\[\[.{1,20}\]\]', rev.text)
    catRedirect2 = re.search(u'#redirect\s{0,2}\[\[.{1,20}\]\]', rev.text)
    catRedirect3 = re.search(u'#Redirect\s{0,2}\[\[.{1,20}\]\]', rev.text)
    if (catRedirect1 is not None):
        some = (catRedirect1.group(0).split(u'[['))[1].split(u']]')[0]
        return some
    elif (catRedirect1 is not None):
        some = (catRedirect2.group(0).split(u'[['))[1].split(u']]')[0]
        return some
    elif (catRedirect3 is not None):
        some = (catRedirect3.group(0).split(u'[['))[1].split(u']]')[0]
        return some
    else:
        return False

    # returns true for birth date


def filter_by_birth(rev):
    bday_format_1 = u"(born\s{0.3}(([0-9])|([0-2][0-9])|([3][0-1]))\s(January|February|March|April|May|June|July|August|September|October|November|December)\s\d{4})"
    bday_format_2 = u"(born\s{0,3}(January|February|March|April|May|June|July|August|September|October|November|December)\s(([0-9])|([0-2][0-9])|([3][0-1])),\s\d{4})"
    #bday_format_3 = "\(born\s\[\[[1-9]{1,2}\s(January|February|March|April|May|June|July|August|September|October|November|December)\]\]\,\s{0,3}\[\[[0-9]{1,4}\]\]"
    bday_format_3 = u"\(born\s{0,1}\[{0,2}[1-9]{1,2}\s{0,3}(january|february|march|april|may|june|july|august|september|october|november|december)\]{0,3}\,{0,1}\s{0,4}\[{0,2}[0-9]{1,4}\]{0,2}"
    born_format_1 = re.search(bday_format_1, rev.text)
    born_format_2 = re.search(bday_format_2, rev.text)
    born_format_3 = re.search(bday_format_3, rev.text.lower())
    #print(born_format_3)
    if (born_format_1 is not None or born_format_2 is not None or born_format_3 is not None):
        return True
    else:
        return False




for page in root.iter(u'{http://www.mediawiki.org/xml/export-0.10/}page'):

    for rev in page.iter(u'{http://www.mediawiki.org/xml/export-0.10/}text'):

        some_value = page.find(u'{http://www.mediawiki.org/xml/export-0.10/}title').text
        print(some_value)
        try:
            #print(some_value)
            person = False
            if (filter_by_redirectIntext(rev) != False):
                # print(filter_by_redirectIntext(rev))
                dict_redict[some_value] = unicode(filter_by_redirectIntext(rev))
                #print(dict_redict)
                print("filter_by_redirectIntext")
                person = False
            elif (filter_by_stub(rev) == True):
                person = True
            elif (filter_by_category(rev)):
                person = True
            elif (filter_by_birth(rev) == True):
                person = True
            elif (filter_by_section(rev) == True):
                person = True
            else:
                person = False
            #print(person)
            if (person == True):
                #print("In Herw")
                isCategory = re.search(u"Category:", some_value)
                #print(isCategory)
                isNumber = re.search(u"[0-9]{1,4}", some_value)
                #print(isNumber)
                isWikiCat = re.search(u"Wikipedia:", some_value)
                #print(isWikiCat)
                isLenCheck34 = len(some_value)
                

                if ((isNumber == None) and 
                (isCategory == None) and 
                (isWikiCat is None) and 
                (isLenCheck34 <=34)):
                  #print("pp")
                  list_names.append(some_value)
                  #print some_value
                else:
                  list_titles.append(some_value)
            else:
                list_titles.append(some_value)

        except:
            # print("Caught in except here : "+str(some_value) )
            continue

for everRedirect in dict_redict.keys():
    if dict_redict[everRedirect] in list_names:
        list_names.append(everRedirect)

#for name in list_names:
 # print name



with open(u"Titles.txt", u"w", encoding=u"UTF8") as f:
    for title in list_titles:
        f.write(title + u"\n")

with open(u"Names.txt", u"w", encoding=u"UTF8") as f:
    for name in list_names:
        f.write(name + u"\n")
