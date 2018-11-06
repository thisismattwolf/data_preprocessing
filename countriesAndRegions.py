# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 16:37:27 2018

@author: Matthew Wolf

===================================
TO DO:
    
    1. Map Devex countries list to other country classifications using coco module

    2. Assign new mappings to different regional mappings

        2b. Check what developing related region classifications we need, add
            as separate lists here.
        
    3. Assign mapping to "worldwide continents" classification
    
    4. Excel / Google Sheets functions to convert from one country scheme
        to another? Or from country to region?
        
    5.
===================================


See google sheet here for Devex reference: 
    https://docs.google.com/spreadsheets/d/1idZ7Tr1d3g7Q7FUGEkdRa5MJ05rnnWpwbfGQ3Ctq0f0/edit#gid=0


"""
devexContinents = ['Africa', 'Asia and Pacific', 'Europe', \
                   'Latin America and Caribbean', 'Middle East', \
                   'North America']

devexRegions = ['Central Africa', 'Eastern Africa', 'Southern Africa', \
                'West Africa', 'Central Asia', 'East Asia and Pacific',\
                'Eastern Europe', 'Latin America and Caribbean', \
                'North Africa and Middle East', 'North America', 'Oceania',\
                'South Asia', 'Western Europe']


devexCountries = ['Burundi', 'Central African Republic', 'Congo', \
                  'Democratic Republic of Congo', 'Rwanda', 'Uganda', \
                  'Afghanistan', 'Armenia', 'Azerbaijan', 'Georgia', \
                  'Kazakhstan', 'Kyrgyzstan', 'Tajikistan', 'Turkmenistan', \
                  'Uzbekistan', 'American Samoa', 'Australia', \
                  'Brunei Darussalam', 'Cambodia', 'China', \
                  'Christmas Island', 'Clipperton Island', \
                  'Cocos (Keeling) Islands', 'Cook Islands', 'Fiji', \
                  'French Polynesia', 'Guam', 'Hong Kong', \
                  'Indonesia', 'Japan', 'Jarvis Island', 'Kiribati', \
                  'Korea', 'Korea', 'Laos', 'Macao', 'Malaysia', \
                  'Marshall Islands', 'Micronesia', 'Midway Islands', \
                  'Mongolia', 'Myanmar', 'Nauru', 'New Caledonia', \
                  'New Zealand', 'Niue', 'Norfolk Island', \
                  'Northern Mariana Islands', 'Palau', 'Palmyra Atoll', \
                  'Papua New Guinea', 'Paracel Islands', 'Philippines', \
                  'Pitcairn', 'Samoa', 'Singapore', 'Solomon Islands', \
                  'Spratly Islands', 'Taiwan', 'Thailand', 'Timor-Leste', \
                  'Tokelau', 'Tonga', 'Tuvalu', 'Vanuatu', 'Viet Nam', \
                  'Wake Island', 'Wallis and Futuna', 'Western Samoa', \
                  'Djibouti', 'Eritrea', 'Ethiopia', 'Kenya', 'Seychelles', \
                  'Somalia', 'Somaliland', 'South Sudan', 'Tanzania', \
                  'Tromelin Island', 'Zanzibar', 'Albania', 'Belarus', \
                  'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', \
                  'Czech Republic', 'Estonia', 'Hungary', 'Kosovo', \
                  'Latvia', 'Lithuania', 'Macedonia (FYROM)', \
                  'Miscellaneous (French)', 'Moldova', 'Montenegro', 'Poland',\
                  'Romania', 'Russian Federation', 'Serbia', 'Slovakia', \
                  'Slovenia', 'Turkey', 'Ukraine', 'Anguilla', \
                  'Antigua and Barbuda', 'Argentina', 'Aruba', 'Bahamas', \
                  'Barbados', 'Belize', 'Bolivia', 'Bonaire', 'Brazil', \
                  'Cayman Islands', 'Chile', 'Colombia', 'Costa Rica', 'Cuba',\
                  'Curacao', 'Dominica', 'Dominican Republic', 'Ecuador', \
                  'El Salvador', 'Falkland Islands (Malvinas)', \
                  'French Guiana', 'Grenada', 'Guadeloupe', 'Guatemala', \
                  'Guyana', 'Haiti', 'Honduras', 'Jamaica', 'Martinique', \
                  'Mexico', 'Montserrat', 'Netherlands Antilles', 'Nicaragua',\
                  'Panama', 'Paraguay', 'Peru', 'Puerto Rico', \
                  'Saint Kitts and Nevis', 'Saint Lucia', \
                  'Saint Vincent and the Grenadines', 'Sint Maarten', \
                  'Suriname', 'Trinidad and Tobago', \
                  'Turks and Caicos Islands', 'U.S. Minor Outlying Islands', \
                  'Uruguay', 'Venezuela', 'Virgin Islands', 'Virgin Islands', \
                  'Algeria', 'Egypt', 'Libya', 'Western Sahara', 'Bahrain', \
                  'Gaza Strip', 'Iran', 'Iraq', 'Israel', 'Jordan', 'Kuwait', \
                  'Lebanon', 'Morocco', 'Oman', 'Palestinian Territory', \
                  'Qatar', 'Saudi Arabia', 'Sudan', 'Syrian Arab Republic', \
                  'Tunisia', 'United Arab Emirates', 'West Bank', 'Yemen', \
                  'Bermuda', 'British Virgin Islands', 'Canada', 'Greenland',\
                  'Howland', 'Navassa Island', 'Saint Pierre and Miquelon', \
                  'United States', 'Baker Island', 'Coral Sea Islands',\
                  'Ashmore and Cartier', 'Bangladesh', 'Bhutan', \
                  'British Indian Ocean Territory', 'Burma', 'East Timor',\
                  'India', 'Maldives', 'Nepal', 'Pakistan', 'Sri Lanka', \
                  'Angola', 'Bassas da India', 'Botswana', 'Comoros', \
                  'Juan de Nova Island', 'Lesotho', 'Madagascar', 'Malawi', \
                  'Mauritius', 'Mayotte', 'Mozambique', 'Namibia', 'Reunion',\
                  'South Africa', 'South Georgia and the South Sandwich Islands', \
                  'Swaziland', 'Zambia', 'Zimbabwe', 'Benin', 'Burkina Faso', \
                  'Cameroon', 'Cape Verde', 'Chad', 'Cote d Ivoire', \
                  'Equatorial Guinea', 'Gabon', 'Gambia', 'Ghana', 'Guinea',\
                  'Guinea-Bissau', 'Liberia', 'Mali', 'Mauritania', 'Niger',\
                  'Nigeria', 'Saint Helena', 'Sao Tome and Principe', \
                  'Senegal', 'Sierra Leone', 'Togo', 'Ã…land Islands',\
                  'Andorra', 'Austria', 'Belgium', 'Cyprus', 'Denmark', \
                  'Faroe Islands', 'Finland', 'France', 'Germany', 'Gibraltar',\
                  'Greece', 'Guernsey', 'Iceland', 'Ireland', 'Isle of Man', \
                  'Italy', 'Jersey', 'Liechtenstein', 'Luxembourg', 'Malta',\
                  'Man', 'Monaco', 'Netherlands', 'Norway', 'Portugal', \
                  'San Marino', 'Spain', 'Svalbard', 'Sweden', 'Switzerland',\
                  'United Kingdom', 'Vatican City State']

