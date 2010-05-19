# Migration utilities and migration steps
from zope.component import getUtility

from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.interfaces.siteroot import IPloneSiteRoot

import logging
logger  = logging.getLogger('prettysociable-migration')


def emptyMigrate(self):
    """For dummy upgrade steps."""
    pass


def migrateTo02(context):
    """Remove wrong kupu styles."""
    site = getUtility(IPloneSiteRoot)
    kupu = getToolByName(site, 'kupu_library_tool', None)

    if kupu is not None:
        paragraph_styles = list(kupu.getParagraphStyles())
    
        wrong_styles = [
            ('prettySociable Link', 'prettySociable|a'),
        ]
        to_remove = dict(wrong_styles)
    
        for style in paragraph_styles:
            css_class = style.split('|')[-1]
            if css_class in to_remove:
                paragraph_styles.remove(style)
                logger.info("Removed style \"%s\" from kupu config." % style)
    
        kupu.configure_kupu(parastyles=paragraph_styles)
