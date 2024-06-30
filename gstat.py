import jc
import jc.parsers.ip_route
import configparser
from subprocess import check_output


def check_routes4(routes_config):
    routes = check_output('ip', '-4', 'route').decode()
    parsed_routes = jc.parse('ip_route', routes)
    
    for rule in routes_config:
        if jc.parse('ip_route', rule):



def main():
    ...



if __name__ == "__main__":
    main()
