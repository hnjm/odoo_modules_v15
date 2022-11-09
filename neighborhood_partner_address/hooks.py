# Copyright 2016 Sodexis
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


def post_init_hook(cr, registry):
    """ Add barrio to address format """
    query = """
        UPDATE res_country
        SET address_format = replace(
        address_format,
        E'%(street2)s\n',
        E'%(street2)s\n%(barrio)s\n'
        )
    """
    cr.execute(query)


def uninstall_hook(cr, registry):
    """ Remove barrio from address format """
    # Remove %(barrio)s\n from address_format
    query = """
        UPDATE res_country
        SET address_format = replace(
        address_format,
        E'%(barrio)s\n',
        ''
        )
    """
    cr.execute(query)

    # Remove %(barrio)s from address_format
    query = """
        UPDATE res_country
        SET address_format = replace(
        address_format,
        E'%(barrio)s',
        ''
        )
    """
    cr.execute(query)
