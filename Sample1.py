from configparser import ConfigParser

config = ConfigParser()

config.read('config.properties')

# Modify the value
# [base_install_dir] section
config.set('base_install_dir', 'base_dir', '/data1/Python_Code/s2o_Python_utility_v1_008/python')

# [sourcedb] section
config.set('sourcedb', 'source.db.driver', '{ODBC Driver 18 for SQL Server}')
config.set('sourcedb', 'source.db.server', 'az-w19-s2o-sql2.rd-plm-devops.bdns.ptc.com')
config.set('sourcedb', 'source.db.dbname', 'WCP4')
config.set('sourcedb', 'source.db.username', 'WCP4')
config.set('sourcedb', 'source.db.schemaname', 'WCP4')
config.set('sourcedb', 'source.db.namedinstance', 'SQL2019')
config.set('sourcedb', 'source.db.connection.max_pool_size', '12')

# [targetdb] section
config.set('targetdb', 'target.db.driver', 'oracle.jdbc.OracleDriver')
config.set('targetdb', 'target.db.server', 'az-qa-cdb-s2o.rd-plm-devops.bdns.ptc.com')
config.set('targetdb', 'target.db.dbname', 'WNCPDB')
config.set('targetdb', 'target.db.username', 'S2O_TEST')
config.set('targetdb', 'target.db.schemaname', 'S2O_TEST')
config.set('targetdb', 'target.db.dbport', '1536')
config.set('targetdb', 'target.db.connection.max_pool_size', '12')


# [other] section
config.set('other', 'wt.home', '/data1/targer/Windchill')
config.set('other', 'wt.java', '/usr/java_1120/jdk-11.0.20')


# Write the changes back to the file
with open('config.properties', 'w') as configfile:
    config.write(configfile)
