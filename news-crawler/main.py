import requests
import xml.etree.ElementTree as ET
from sitemap import parse_sitemap
from extractor import extract_text_from_url
import pandas as pd
from data_elastic import elastic_sitemap


elastic_sitemap("https://primates.dev/sitemap.xml",["loc", "lastmod"])




