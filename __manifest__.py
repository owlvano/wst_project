{
    'name': "WST Project",
    'version': "1.0.0",
    'author': "Ivan Sova / Sythil Tech",
    'category': "Tools",
    'summary': "support_ticket module extension",
    'description': "A 'support_ticket' module extension to implement 'project' module fuctionality to support tickets",
    'website':'https://www.odoo.com/apps/modules/10.0/website_support/',
    'license':'LGPL-3',
    'data': [
        'views/project_views.xml',
        'views/website_support_settings_views.xml',
        'views/website_support_ticket_views.xml',        
    ],
    'demo': [],
    'depends': ['support_ticket', 'project'],
    'installable': True,
}