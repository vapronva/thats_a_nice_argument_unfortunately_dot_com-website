from ipaddress import IPv4Address
import random
from IPInfoAPI import IPInfoResponse
from IPInfoAPI import IPInfoAPI
from faker import Faker
from faker.providers import internet as faker_internet
from faker.providers import company as faker_company
from faker.providers import ssn as faker_ssn
import subprocess
from ProxyCheckAPI import ProxyCheckAPI, ProxyCheckAnswerModel


class NonsenseIPInformationGenerator:
    """
    Get random information about the given IP!
    """

    def __init__(self, iia: IPInfoAPI, pca: ProxyCheckAPI) -> None:
        """
        Initialize the class.

        Args:
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
        """
        Get a random DNS provider.

        Returns:
            str: IP address of the DNS provider.
        """
        _dnsproviders = ["1.1.1.1", "9.9.9.9", "8.8.8.8", "45.90.28.100", "45.90.30.100",
                         "208.67.222.222", "208.67.220.220", "64.6.64.6", "64.6.65.6",
                         "195.46.39.39", "195.46.39.40", "8.26.56.26", "8.20.247.20",
                         "77.88.8.8", "77.88.8.1"]
        return random.choice(_dnsproviders)

    @staticmethod
    def getRandomCompanyRouterName() -> str:
        """
        Get a random company router name.

        Returns:
            str: Router's company name.
        """
        _companies = ["TP-Link", "Xiaomi", "Netgear", "MikroTik", "Netgate",
                      "Cisco", "Linksys", "Fortinet", "ASUS", "Tenda", "Netis",
                      "SonicWall", "Apple", "ECPN", "GL.iNet", "Ubiquiti", "Huawei"]
        return random.choice(_companies)

    @staticmethod
    def getRandomDeviceVendorCompany() -> str:
        """
        Get a random device vendor company.

        Returns:
            str: Device vendor company.
        """
        _companies = ["Apple", "Lenovo", "Dell", "HP", "Acer", "Asus", "Samsung", "Toshiba",
                      "Nintendo", "Sony", "Microsoft", "Intel", "AMD", "IBM", "Oracle",
                      "Sony", "Apple", "Lenovo", "Dell", "HP", "Acer", "Asus", "Samsung"]
        return random.choice(_companies)

    def generateRandomPortForwardingConnectionsLikeMKT(self) -> str:
        """
        Generate a random port forwarding connection.

        Args:
            ip (IPv4Address): The IP address.

        Returns:
            str: The port forwarding connection string.
        """
        return f"[{random.choice(['HTTP', 'TCP', 'UDP'])}] {self.__faker.ipv4_private(address_class='c')}:{self.__faker.port_number(is_system=self.__faker.boolean(), is_user=self.__faker.boolean(), is_dynamic=self.__faker.boolean())} => {self.__faker.ipv4_private(address_class='c')}:{self.__faker.port_number(is_system=self.__faker.boolean(), is_user=self.__faker.boolean(), is_dynamic=self.__faker.boolean())}"

    def generate(self, userIP: IPv4Address) -> list:
        """
        Generate a random nonsense information for the given IP.

        Args:
            userIP (IPv4Address): User's IP address.

        Returns:
            list: A list of random nonsense information.
        """
        Faker.seed(random.randint(0, 100000))
        ipinfo: IPInfoResponse = self.__iia.getInfo(userIP)
        proxycheck: ProxyCheckAnswerModel = self.__pca.getInfo(userIP)
        bllngrr = []
        bllngrr.append(f"IP: {ipinfo.ip}")
        bllngrr.append("N: " + str(ipinfo.loc.split(",")[0]))
        bllngrr.append("W: " + str(ipinfo.loc.split(",")[1]))
        bllngrr.append(f"SS Number: {self.__faker.ssn()}")
        bllngrr.append(f"IPv6: {self.__faker.ipv6()}")
        bllngrr.append(f"UPNP: {'Enabled' if self.__faker.boolean() else 'Disabled'}")
        bllngrr.append("DMZ: " + str(self.__faker.ipv4_private(address_class="b")))
        bllngrr.append(f"MAC: {self.__faker.mac_address()}")
        bllngrr.append(f"ISP: {ipinfo.org}")
        bllngrr.append(f"DNS: {self.getRandomDNSProvider()}")
        bllngrr.append(f"ALT DNS: {self.getRandomDNSProvider()}")
        bllngrr.append(f"DNS SUFFIX: {self.__faker.company()}")
        bllngrr.append("WAN: " + str(self.__faker.ipv4_private(address_class="a")))
        bllngrr.append(f"WAN TYPE: {proxycheck.type}")
        bllngrr.append("GATEWAY: " + str(self.__faker.ipv4_private(address_class="c")))
        bllngrr.append("SUBNET MASK: 255.255.255.0")
        bllngrr.append("UDP OPEN PORTS: " + ", ".join(
            [str(self.__faker.port_number(is_user=True)) for i in range(
                random.randint(2,4))]))
        bllngrr.append("TCP OPEN PORTS: " + ", ".join(
            [str(self.__faker.port_number(is_system=True)) for i in range(
                random.randint(1,3))]))
        bllngrr.append(f"ROUTER VENDOR: {self.getRandomCompanyRouterName()}")
        bllngrr.append(f"DEVICE VENDOR: {self.getRandomDeviceVendorCompany()}")
        bllngrr.append("CONNECTION TYPE: " + str(
            self.__faker.random_element(elements=[
                "PPTP", "L2TP", "PPPoE", "PPPoA", "DHCP", "Static", "Dynamic", "DNS",
                "DNS-DHCP", "DNS-Static", "DNS-Dynamic"])))
        bllngrr.append("ICMP HOPS:")
        ayoNumberOfHops = random.randint(5,9)
        for _ in range(ayoNumberOfHops):
            if self.__faker.boolean():
                bllngrr.append(str(self.__faker.ipv4_private(
                    address_class="a" if self.__faker.boolean() else "b")))
            else:
                bllngrr.append(str(self.__faker.hostname()))
        bllngrr.append(f"TOTAL HOPS: {ayoNumberOfHops}")
        for _ in range(random.randint(6,9)):
            bllngrr.append(self.generateRandomPortForwardingConnectionsLikeMKT())
        bllngrr.append(f"EXTERNAL MAC: {self.__faker.mac_address()}")
        bllngrr.append("MODEM JUMPS: 64")
        return bllngrr
