fixture_check_document_existance = [("2207 876234", True),
                           ('567453', False),
                           ("10006", True),
                           ('7645427', False)]

fixture_get_doc_owner_name = [("2207 876234", 'Василий Гупкин'),
                              ("10006", "Аристарх Павлов")]

fixture_test_remove_doc_from_shelf = ['2207 876234']

fixture_add_new_shelf = [('1', False, None),
                         ('5', True, None),
                         (None, False, '1'),
                         (None, True, '6')]

fixture_append_doc_to_shelf = [('3333333', '1'),
                               ('44444444', '2'),
                               ('5555555', '3')]

fixture_delete_doc = [("16", True),
                      ('555555', None)]

fixture_get_doc_shelf = [('11-2', '1'),
                         ('10006', '2'),
                         ('66', None)]

fixture_add_new_doc = [('56743', 'p', 'AA', '1'),
                       ('45676', 'ff', 'dfdf', '3')]

