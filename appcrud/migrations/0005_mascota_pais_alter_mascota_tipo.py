# Generated by Django 5.0.6 on 2024-06-03 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcrud', '0004_alter_mascota_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='pais',
            field=models.CharField(choices=[('CM', 'CAMERUN'), ('DZ', 'ARGELIA'), ('KR', 'REP. COREA'), ('DK', 'DINAMARCA'), ('ZA', 'SUD AFRICA'), ('AO', 'ANGOLA'), ('CY', 'CHIPRE'), ('CI', 'COSTA DE MARFIL'), ('DM', 'DOMINICA'), ('LK', 'SRI LANKA'), ('UY', 'URUGUAY'), ('SN', 'SENEGAL'), ('GT', 'GUATEMALA'), ('GD', 'GRANADA'), ('JE', 'JERSEY'), ('JP', 'JAPON'), ('KY', 'ISLAS CAIMAN'), ('ME', 'MONTENEGRO'), ('TT', 'TRINIDAD TOBAGO'), ('GG', 'GUERNSEY'), ('SL', 'SIERRA LEONE'), ('AE', 'EMIRATOS ARABES'), ('BO', 'BOLIVIA'), ('BB', 'BARBADOS'), ('BA', 'BOSNIA'), ('BZ', 'BELICE'), ('SA', 'ARABIA SAUDITA'), ('MA', 'MARRUECOS'), ('CR', 'COSTA RICA'), ('SG', 'SINGAPUR'), ('BJ', 'BENIN'), ('IL', 'ISRAEL'), ('ZR', 'ZAIRE'), ('IG', 'INGLATERRA'), ('JO', 'JORDANIA'), ('CA', 'CANADA'), ('FR', 'FRANCIA'), ('TW', 'TAIWAN'), ('VG', 'ISLAS VIRGENES BRITANICAS'), ('MZ', 'MOZAMBIQUE'), ('MR', 'MAURITANIA'), ('RS', 'SERBIA'), ('RU', 'RUSIA'), ('KP', 'REP. DEM. COREA'), ('AU', 'AUSTRALIA'), ('EE', 'ESTONIA'), ('IQ', 'IRAQ'), ('PS', 'PALESTINA'), ('SR', 'SURINAM'), ('UZ', 'REPUBLICA DE UZBEKISTAN'), ('PL', 'POLONIA'), ('BE', 'BELGICA'), ('HT', 'HAITI'), ('EG', 'EGIPTO'), ('CO', 'COLOMBIA'), ('EC', 'ECUADOR'), ('AR', 'ARGENTINA'), ('AS', 'SAMOA AMERICANA'), ('KZ', 'KAZAJISTAN'), ('MY', 'MALASIA'), ('GY', 'GUYANA'), ('CV', 'CABO VERDE'), ('OM', 'OMAN'), ('PE', 'PERU'), ('BM', 'BERMUDAS'), ('LU', 'LUXEMBURGO'), ('LB', 'LIBANO'), ('PA', 'PANAMA'), ('MU', 'MAURICIO'), ('NZ', 'NUEVA ZELANDIA'), ('BR', 'BRASIL'), ('GH', 'GHANA'), ('SE', 'SUECIA'), ('CN', 'CHINA'), ('GA', 'GABON'), ('HK', 'HONG KONG'), ('NA', 'NAMIBIA'), ('MN', 'MONGOLIA'), ('IN', 'INDIA'), ('IS', 'ISLANDIA'), ('GR', 'GRECIA'), ('JM', 'JAMAICA'), ('SD', 'SUDAN'), ('SO', 'SOMALIA'), ('AF', 'AFGANISTAN'), ('HU', 'HUNGRIA'), ('BY', 'REPUBLICA DE BELARUS'), ('CL', 'CHILE'), ('NP', 'NEPAL'), ('TH', 'TAILANDIA'), ('KW', 'KUWAIT'), ('UA', 'UCRANIA'), ('AZ', 'REPUBLICA DE AZERBAIYAN'), ('NG', 'NIGERIA'), ('MT', 'MALTA'), ('PR', 'PUERTO RICO'), ('QA', 'QATAR'), ('NO', 'NORUEGA'), ('RO', 'RUMANIA'), ('SM', 'SAN MARINO'), ('AN', 'ANTILLAS HOLAND'), ('HR', 'CROACIA'), ('CH', 'SUIZA'), ('SI', 'ESLOVENIA'), ('TJ', 'TAYIKISTAN'), ('ZM', 'ZAMBIA'), ('SY', 'REP.ARABE SIRIA'), ('ES', 'ESPAÑA'), ('GB', 'GRAN BRETAÑA'), ('LR', 'LIBERIA'), ('PH', 'FILIPINAS'), ('IR', 'IRAN'), ('VE', 'VENEZUELA'), ('DO', 'REP DOMINICANA'), ('HN', 'HONDURAS'), ('US', 'ESTADOS UNIDOS'), ('KE', 'KENYA'), ('MC', 'MONACO'), ('MH', 'ISLAS MARSHALL'), ('MX', 'MEXICO'), ('NL', 'HOLANDA'), ('AT', 'AUSTRIA'), ('CG', 'CONGO'), ('ID', 'INDONESIA'), ('BH', 'REINO DE BAHREIN'), ('CU', 'CUBA'), ('IE', 'IRLANDA'), ('SK', 'ESLOVAKIA'), ('AL', 'ALBANIA'), ('GE', 'GEORGEA'), ('BG', 'BULGARIA'), ('BS', 'BAHAMAS'), ('DE', 'ALEMANIA'), ('PT', 'PORTUGAL'), ('VI', 'ISLAS VIRGENES (U.S)'), ('IM', 'ISLA DE MAN'), ('TR', 'TURQUIA'), ('VN', 'VIETNAM'), ('Sin asignar', 'Sin asignar'), ('AM', 'ARMENIA'), ('NI', 'NICARAGUA'), ('CX', 'CURAZAO'), ('IT', 'ITALIA'), ('SV', 'EL SALVADOR'), ('PK', 'PAKISTAN'), ('PY', 'PARAGUAY'), ('FI', 'FINLANDIA'), ('CZ', 'REPUBLICA CHECA')], default='Sin asignar', max_length=50),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='tipo',
            field=models.CharField(choices=[('CONEJO', 'Conejo'), ('PERRO', 'Perro'), ('ANACONDA', 'Anaconda'), ('GATO', 'Gato'), ('OTRO', 'Otro')], default='OTRO', max_length=50),
        ),
    ]
