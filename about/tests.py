from django.test import TestCase
from .models import Banner, AboutSection, Service, TechnologyIndex, TeamMember, Location

class BannerModelTest(TestCase):
    def setUp(self):
        Banner.objects.create(
            title="About Us Banner",
            description="This is a banner description.",
            button_link="https://example.com"
        )

    def test_banner_creation(self):
        banner = Banner.objects.get(title="About Us Banner")
        self.assertEqual(banner.title, "About Us Banner")
        self.assertEqual(str(banner), "About Us")
        
class AboutSectionModelTest(TestCase):
    def setUp(self):
        AboutSection.objects.create(
            title="About Section",
            sub_desc="Short description about section.",
            description="This is a detailed description of the about section."
        )

    def test_about_section_creation(self):
        section = AboutSection.objects.get(title="About Section")
        self.assertEqual(section.title, "About Section")
        self.assertEqual(str(section), "About Our Online Store")
        
class ServiceModelTest(TestCase):
    def setUp(self):
        Service.objects.create(
            title="Service 1",
            description="This is the description of the first service.",
            icon_class="fa-icon",
            step_number=1
        )

    def test_service_creation(self):
        service = Service.objects.get(title="Service 1")
        self.assertEqual(service.title, "Service 1")
        self.assertEqual(service.step_number, 1)
        self.assertEqual(str(service), "HOW IT WORKS")

class TechnologyIndexModelTest(TestCase):
    def setUp(self):
        TechnologyIndex.objects.create(
            title="Technology 1",
            description="This is a technology description.",
            active_clients=10,
            projects_done=20,
            team_advisors=5,
            users_online=50
        )

    def test_technology_index_creation(self):
        technology = TechnologyIndex.objects.get(title="Technology 1")
        self.assertEqual(technology.title, "Technology 1")
        self.assertEqual(technology.active_clients, 10)
        self.assertEqual(str(technology), "Technology Index")

class TeamMemberModelTest(TestCase):
    def setUp(self):
        TeamMember.objects.create(
            name="John Doe",
            position="Developer",
            descr="Senior Developer at XYZ",
            facebook="https://facebook.com/johndoe"
        )

    def test_team_member_creation(self):
        member = TeamMember.objects.get(name="John Doe")
        self.assertEqual(member.name, "John Doe")
        self.assertEqual(str(member), "THE TEAM")

class LocationModelTest(TestCase):
    def setUp(self):
        Location.objects.create(
            address="123 Main St",
            city="Kathmandu",
            country="Nepal",
            map_link="https://maps.example.com",
            phone="+977123456789",
            email="example@example.com"
        )

    def test_location_creation(self):
        location = Location.objects.get(city="Kathmandu")
        self.assertEqual(location.city, "Kathmandu")
        self.assertEqual(str(location), "123 Main St, Kathmandu")
