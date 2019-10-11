#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def face(url):
    options = Options()
    prefs = {'profile.default_content_setting_values': {'cookies': 2, 'images': 2, 'plugins': 2, 'popups': 2,
                                                        'geolocation': 2, 'notifications': 2,
                                                        'auto_select_certificate': 2, 'fullscreen': 2, 'mouselock': 2,
                                                        'mixed_script': 2, 'media_stream': 2, 'media_stream_mic': 2,
                                                        'media_stream_camera': 2, 'protocol_handlers': 2,
                                                        'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2,
                                                        'push_messaging': 2, 'ssl_cert_decisions': 2,
                                                        'metro_switch_to_desktop': 2, 'protected_media_identifier': 2,
                                                        'app_banner': 2, 'site_engagement': 2, 'durable_storage': 2}}
    options.add_experimental_option('prefs', prefs)
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument('--headless')
    dr = webdriver.Chrome("C:/Users/DS-18-D3-023/Desktop/ChromDriver/chromedriver.exe",chrome_options=options)
    dr.get(url)
    good = dr.find_element_by_css_selector(
        '#spiLayer > div._reactionModule.u_likeit > ul > li.u_likeit_list.good > a > span.u_likeit_list_count._count')
    nice = dr.find_element_by_css_selector(
        '#spiLayer > div._reactionModule.u_likeit > ul > li.u_likeit_list.warm > a > span.u_likeit_list_count._count')
    sad = dr.find_element_by_css_selector(
        '#spiLayer > div._reactionModule.u_likeit > ul > li.u_likeit_list.sad > a > span.u_likeit_list_count._count')
    angry = dr.find_element_by_css_selector(
        '#spiLayer > div._reactionModule.u_likeit > ul > li.u_likeit_list.angry > a > span.u_likeit_list_count._count')
    wanted = dr.find_element_by_css_selector(
        '#spiLayer > div._reactionModule.u_likeit > ul > li.u_likeit_list.want > a > span.u_likeit_list_count._count')
    recommand = dr.find_element_by_css_selector('#toMainContainer > a > em.u_cnt._count')
    if recommand.text=='':
        x='0'
    else:
        x=recommand.text
    return good.text, nice.text, sad.text, angry.text, wanted.text,x