import random
from ipaddress import IPv4Address

from faker import Faker
from faker.providers import company as faker_company
from faker.providers import internet as faker_internet
from faker.providers import ssn as faker_ssn
from IPInfoAPI import IPInfoAPI, IPInfoResponse
from ProxyCheckAPI import ProxyCheckAnswerModel, ProxyCheckAPI


class NonsenseIPInformationGenerator:
    """Get random information about the given IP!."""

    def __init__(self, iia: IPInfoAPI, pca: ProxyCheckAPI) -> None:
        """Initialize the class.

        Args:
        ----
            iia (IPInfoAPI): IPInfoAPI instance.
            pca (ProxyCheckAPI): ProxyCheckAPI instance.
        """
        self.__iia = iia
        self.__pca = pca
        self.__faker = Faker()
        self.__faker.add_provider(faker_internet)
        self.__faker.add_provider(faker_company)
        self.__faker.add_provider(faker_ssn)

    @staticmethod
    def getRandomDNSProvider() -> str:
        """Get a random DNS provider.

        Returns
        -------
            str: IP address of the DNS provider.
        """
        _dnsproviders = [
            "1.1.1.1",
            "9.9.9.9",
            "8.8.8.8",
            "45.90.28.100",
            "45.90.30.100",
            "208.67.222.222",
            "208.67.220.220",
            "64.6.64.6",
            "64.6.65.6",
            "195.46.39.39",
            "195.46.39.40",
            "8.26.56.26",
            "8.20.247.20",
            "77.88.8.8",
            "77.88.8.1",
        ]
        return random.choice(_dnsproviders)

    @staticmethod
    def getRandomCompanyRouterName() -> str:
        """Get a random company router name.

        Returns
        -------
            str: Router's company name.
        """
        _companies = [
            "TP-Link",
            "Xiaomi",
            "Netgear",
            "MikroTik",
            "Netgate",
            "Cisco",
            "Linksys",
            "Fortinet",
            "ASUS",
            "Tenda",
            "Netis",
            "SonicWall",
            "Apple",
            "ECPN",
            "GL.iNet",
            "Ubiquiti",
            "Huawei",
        ]
        return random.choice(_companies)

    @staticmethod
    def getRandomDeviceVendorCompany() -> str:
        """Get a random device vendor company.

        Returns
        -------
            str: Device vendor company.
        """
        _companies = [
            "Apple",
            "Lenovo",
            "Dell",
            "HP",
            "Acer",
            "Asus",
            "Samsung",
            "Toshiba",
            "Nintendo",
            "Sony",
            "Microsoft",
            "Intel",
            "AMD",
            "IBM",
            "Oracle",
            "Sony",
            "Apple",
            "Lenovo",
            "Dell",
            "HP",
            "Acer",
            "Asus",
            "Samsung",
        ]
        return random.choice(_companies)

    def generateRandomPortForwardingConnectionsLikeMKT(self) -> str:
        """Generate a random port forwarding connection.

        Args:
        ----
            ip (IPv4Address): The IP address.

        Returns:
        -------
            str: The port forwarding connection string.
        """
        return f"""[{random.choice(['HTTP', 'TCP', 'UDP'])}] \
{self.__faker.ipv4_private(address_class='c')}:\
{self.__faker.port_number(
    is_system=self.__faker.boolean(),
    is_user=self.__faker.boolean(),
    is_dynamic=self.__faker.boolean())} => \
{self.__faker.ipv4_private(address_class='c')}:\
{self.__faker.port_number(
    is_system=self.__faker.boolean(),
    is_user=self.__faker.boolean(),
    is_dynamic=self.__faker.boolean())}"""

    def generate(self, userIP: IPv4Address, disableICMPhopsInfo: bool) -> list:
        """Generate a random nonsense information for the given IP.

        Args:
        ----
            userIP (IPv4Address): User's IP address.

        Returns:
        -------
            list: A list of random nonsense information.
        """
        Faker.seed(random.randint(0, 100000))
        ipinfo: IPInfoResponse = self.__iia.getInfo(userIP)
        proxycheck: ProxyCheckAnswerModel = self.__pca.getInfo(userIP)
        bllngrr = [
            f"IP: {ipinfo.ip}",
            "N: " + str(ipinfo.loc.split(",")[0]),
            "W: " + str(ipinfo.loc.split(",")[1]),
            f"SS Number: {self.__faker.ssn()}",
            f"IPv6: {self.__faker.ipv6()}",
            f"UPNP: {'Enabled' if self.__faker.boolean() else 'Disabled'}",
            "DMZ: " + str(self.__faker.ipv4_private(address_class="b")),
            f"MAC: {self.__faker.mac_address()}",
            f"ISP: {ipinfo.org}",
            f"DNS: {self.getRandomDNSProvider()}",
            f"ALT DNS: {self.getRandomDNSProvider()}",
            f"DNS SUFFIX: {self.__faker.company()}",
            "WAN: " + str(self.__faker.ipv4_private(address_class="a")),
            f"WAN TYPE: {proxycheck.type}",
            "GATEWAY: " + str(self.__faker.ipv4_private(address_class="c")),
            "SUBNET MASK: 255.255.255.0",
            "UDP OPEN PORTS: "
            + ", ".join(
                [
                    str(self.__faker.port_number(is_user=True))
                    for _ in range(random.randint(2, 4))
                ],
            ),
            "TCP OPEN PORTS: "
            + ", ".join(
                [
                    str(self.__faker.port_number(is_system=True))
                    for _ in range(random.randint(1, 3))
                ],
            ),
            f"ROUTER VENDOR: {self.getRandomCompanyRouterName()}",
            f"DEVICE VENDOR: {self.getRandomDeviceVendorCompany()}",
            "CONNECTION TYPE: "
            + str(
                self.__faker.random_element(
                    elements=[
                        "PPTP",
                        "L2TP",
                        "PPPoE",
                        "PPPoA",
                        "DHCP",
                        "Static",
                        "Dynamic",
                        "DNS",
                        "DNS-DHCP",
                        "DNS-Static",
                        "DNS-Dynamic",
                    ],
                ),
            ),
        ]
        if not disableICMPhopsInfo:
            bllngrr.append("ICMP HOPS:")
            ayoNumberOfHops = random.randint(5, 9)
            for _ in range(ayoNumberOfHops):
                if self.__faker.boolean():
                    bllngrr.append(
                        str(
                            self.__faker.ipv4_private(
                                address_class="a" if self.__faker.boolean() else "b",
                            ),
                        ),
                    )
                else:
                    bllngrr.append(str(self.__faker.hostname()))
            bllngrr.append(f"TOTAL HOPS: {ayoNumberOfHops}")
        valueToBeDecremented = 4 if disableICMPhopsInfo else 0
        bllngrr.extend(
            self.generateRandomPortForwardingConnectionsLikeMKT()
            for _ in range(
                random.randint(6 - valueToBeDecremented, 8 - valueToBeDecremented),
            )
        )
        bllngrr.extend(
            (f"EXTERNAL MAC: {self.__faker.mac_address()}", "MODEM JUMPS: 64"),
        )
        return bllngrr
