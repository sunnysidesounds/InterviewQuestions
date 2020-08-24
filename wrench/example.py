
def page_name(string, site_map):

    breadcrumbs = []
    breadcrumbs.append(site_map['name'])
    page_name_helper(string, site_map['subPages'], breadcrumbs)
    return breadcrumbs


def page_name_helper(string, site_map, breadcrumbs):

    for i in range(len(site_map)):
        value = site_map[i]['name']

        if 'subPages' in site_map[i]:
            breadcrumbs.append(value)
            return page_name_helper(string, site_map[i]['subPages'], breadcrumbs)
        else:
            if value == string:
                breadcrumbs.append(value)
            else:
                return page_name_helper(string, site_map[i]['subPages'], breadcrumbs)


if __name__ == '__main__':

    site_map = {
        "name": "Home",
        "subPages": [
            {
                "name": "Appointments",
                "subPages":[
                    {
                        "name":"Past Appointments",
                        "subPages":[
                            {
                                "name":"Receipt",
                                "subPages":[

                                ]
                            },
                            {
                                "name":"Service Report",
                                "subPages":[
                                    {
                                        "name":"Printable Service Report",
                                        "subPages":[

                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "name":"Active Appointments",
                        "subPages":[

                        ]
                    },
                    {
                        "name": "Past Appointments",
                        "subPages": [

                        ]
                    }
                ]
            },
            {
                "name": "Quotes",
                "subPages":[

                ]
            },
            {
                "name": "Book Job",
                "subPages": [

                ]
            }
        ]
    }

    results_list = page_name("Receipt", site_map)
    if results_list == ['Home', 'Appointments', 'Past Appointments', 'Receipt']:
        print("True ", results_list)






















