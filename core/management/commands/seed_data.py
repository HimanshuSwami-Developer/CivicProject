from django.core.management.base import BaseCommand

from core.models import Cause, Donation, Feedback, NewsArticle, Project


class Command(BaseCommand):
    help = "Seed the database with demo data matching the Sankalp Adhikar Vishwas Ekta Party design mockups."

    def handle(self, *args, **options):
        if Cause.objects.exists():
            self.stdout.write("Data already seeded, skipping.")
            return

        causes = [
            Cause.objects.create(
                name="Street Dogs Shelter",
                description="Rescue, medical care, and rehoming projects for the community's street dogs.",
                icon="pets",
                image_url="https://lh3.googleusercontent.com/aida-public/AB6AXuB3Ltx88C5zfwFeXag5TWDlBYufwmRupLlpEshytRfFOo1p9jRMC_O5kH21fGOCbzy2v-LtDu-pOpWLl96GsMiLW5VUHQGrG4i6ik9UHxXd0O6YD52WMJ4zw_Q7oOTiDX26uLlNWMFLQokqPdsf8xbS0kWKKTLKsw92qd5PDaAwPFPiS4zsZ69G_Mqmksvm44bU9SzXMURcIlNhF3AikYs_ZQmZWH3n1jiq2gEBax1XRgUK9FRIkrJn",
                goal_amount=50000,
                raised_amount=32500,
            ),
            Cause.objects.create(
                name="Empower Orphans",
                description="Education, nutrition, and psychological support for orphaned children.",
                icon="child_care",
                image_url="https://lh3.googleusercontent.com/aida-public/AB6AXuAr3OSVOWXCeIRQ5PrxLbDVl7Vhou758ovM7gGCdqyT0M7hVUWgX8X05kPlTua8cz7DUAq1rnhZxHLxk4KhNCgc5mTUKds7ekxjXim9loeYTnJ7qcTM3llAkfu-K3jBwC9IEA-SFzuY6LpPmdHJqw8Tbio_nwvX9HVAf2aevFskZsEgrIoVfu1rDSYI3UAs-N3RNqynf1rTkSi0xJAq7pOseXMw7tB3nXttBsZovLlcpRJAYCMhaJHs",
                goal_amount=100000,
                raised_amount=64000,
            ),
            Cause.objects.create(
                name="General Fund",
                description="Powering our campaigns, grassroots organizing, and administrative efforts.",
                icon="campaign",
                goal_amount=0,
                raised_amount=0,
            ),
            Cause.objects.create(
                name="School Infrastructure",
                description="Modernizing school buildings and classroom equipment.",
                icon="school",
                goal_amount=60000,
                raised_amount=50000,
            ),
            Cause.objects.create(
                name="Medical Outreach",
                description="Mobile clinics and preventive care for underserved neighborhoods.",
                icon="medical_services",
                goal_amount=40000,
                raised_amount=18000,
            ),
        ]

        Project.objects.create(
            title="Clean Water Initiative",
            category="Infrastructure",
            description="Providing sustainable, long-term access to clean drinking water for underserved rural communities through advanced filtration technology.",
            image_url="https://lh3.googleusercontent.com/aida-public/AB6AXuBLgpwmeB6wI9hWcV6RPAA2BIzG5z86h-CSnaurWQ1IVCDtIFkkw6T48X7Sb1WstoT8SK5K_IIDbn6SlMIsZKrJgNMdH_dmP86lugPADiKPKqSlViQ5fRRHOlWl5e6js_DYe0iTlmDUYhUdOd6OCaLcUK-SiFET2Nz0RlxcCAV0XmFLOFhhOpx-AQxUggKegcrhYlB08JEktz250fwMulr6ZhfohYqQibWOmAevkNS3CN3q1g09kd93",
            goal_amount=200000,
            raised_amount=150000,
            progress_percent=75,
            status="on_track",
            priority="Critical Priority",
            is_featured=True,
        )
        Project.objects.create(
            title="Youth Education Program",
            category="Education",
            description="Equipping the next generation with digital literacy and vocational skills essential for the modern global economy.",
            image_url="https://lh3.googleusercontent.com/aida-public/AB6AXuCBdKN3-STI6YULPDHn1apnK0rDiMZYeUBF_1CZGYqPaClLxQhuVU3jiW3pJgIMaTix7IvlshQGAe7lnMpBiNgWXyrRHmJ3ExYpXr8N3Wn8-A0fDV41mJ6Q1JST5wWQ16PY2nlZRAAFXNFemfd3lVGyMiB8INsuKnbIv2urea_Bx50jZjjrWwlAn-zYdlcYAEmwz7x3tu4-K9KPFtwkh2V8poQInpFbgOt7_YMUnQbyMcKEPe01X-Uj",
            goal_amount=50000,
            raised_amount=12900,
            progress_percent=26,
            status="on_track",
        )
        Project.objects.create(
            title="Rural Infrastructure",
            category="Infrastructure",
            description="Expanding transport links and digital connectivity to bridge the gap between rural production and urban markets.",
            image_url="https://lh3.googleusercontent.com/aida-public/AB6AXuC-YXCTWuz9B32mZcYDHe4aeoT6v5UoP-dk2_CrSXIhY1k6st1DlhVfJU4zTF1HQnwNE2XO8gXWMf4kC4ogKXptKm-jgW6pBihFX-aOTQ2yGHsuaykHcnLrkYKzQ8EnltAKcTW9I0k9IxVCBlMvqsBiU-8MUsaqLVXhvTZLVcwDZOLipp3dcixyTbRDs-9k4LJEiHOJ9O8TDCAtGG_12hDXaPEC58HruOHXcKZw4iIAuDxmGnTtZrbO",
            goal_amount=300000,
            raised_amount=270000,
            progress_percent=90,
            status="on_track",
        )
        Project.objects.create(
            title="Urban Renewal Initiative",
            category="Infrastructure",
            description="Revitalizing downtown corridors with sustainable infrastructure and community-focused public spaces.",
            image_url="https://lh3.googleusercontent.com/aida-public/AB6AXuAhXvxX36oNCGuU9E80PMRh3boaY6vCiQ-h032T0RHFYaEawDVzyMjkNILvf5dQFXUa8Z4GTM1pax9Rq1xtRIa984eY2jgd2GchMg6LrnI_JfZ1a8jMt9E39ITv10xUrhOwcxN1rpbrPrKKJrLhFxH57gK4atyceoSE1mm1fe2EMHT5kqTRtC96Vjy9sYYoLxKOYH9Lf3b9ra9sCvDicM57CAkbKGNjv74tBGNhV9ZqSLfs7nA7BSN_",
            goal_amount=125000,
            raised_amount=84200,
            progress_percent=67,
            status="on_track",
        )
        Project.objects.create(
            title="Digital Literacy Program",
            category="Education",
            description="Providing advanced STEM equipment and resources to underfunded local school districts.",
            image_url="https://lh3.googleusercontent.com/aida-public/AB6AXuCz0evH8IVD35UDIkcEvlLvac-WW82ksVPa6G0ZA0y1uv8m9f-TlOE2-rGTSahrRuxYHlIeiWQMeSABX3YVjHK7YdVQ1FJ-bTzvscrEvO_0PMEOcdYWs5EjbRnaOKBHaPQDsN0asry3jlW9gCIC1BpfNQNCD7zQDgiHd255Fob94bXvOAniAEG60D8fq_kjFkSBT2DRM13EVBEEkIDFPk2DSk3tdWyJn9VQgmQvZs3VJ6zm4JG2P793",
            goal_amount=80000,
            raised_amount=17600,
            progress_percent=22,
            status="at_risk",
        )
        Project.objects.create(
            title="Clean Water Filtration Plant",
            category="Infrastructure",
            description="Finalizing the filtration plant for the Northeast region. Every dollar now goes directly to maintenance training.",
            image_url="",
            goal_amount=90000,
            raised_amount=81000,
            progress_percent=90,
            status="completed",
        )

        street_dogs, orphans, general, school, medical = causes

        Donation.objects.create(donor_name="Jane Smith", email="jane.smith@email.com", amount=2500, cause=street_dogs, status="success")
        Donation.objects.create(donor_name="Arthur Morgan", email="a.morgan@frontier.org", amount=150, cause=orphans, status="pending")
        Donation.objects.create(donor_name="Bruce Wayne", email="bruce@wayneent.com", amount=50000, cause=school, status="success")
        Donation.objects.create(donor_name="John Doe", email="j.doe@anon.com", amount=45, cause=street_dogs, status="failed")
        Donation.objects.create(donor_name="Linda Hamilton", email="linda.h@techcorp.io", amount=1200, cause=medical, status="success")
        Donation.objects.create(donor_name="Anonymous Donor", email="", amount=5000, cause=general, status="success")

        Feedback.objects.create(
            type="suggestion",
            name="Sarah Jenkins",
            email="s.jenkins@citymail.com",
            category="infrastructure",
            message="I noticed that the new Central Library has a vast, south-facing roof area that seems completely underutilized. Installing a solar array there could potentially power the entire building and act as an educational showcase for the city's green initiatives.",
            status="new",
        )
        Feedback.objects.create(
            type="suggestion",
            name="Marcus Chen",
            email="mchen99@web.net",
            category="infrastructure",
            message="The current Farmers Market on 4th Ave is a huge success, but it's becoming dangerously overcrowded on Saturday mornings. We should consider closing off 5th Ave as well during market hours.",
            status="in_review",
        )
        Feedback.objects.create(
            type="complaint",
            name="Dave Miller",
            email="dmiller@home.org",
            category="safety",
            message="The streetlamp directly in front of 42 Elm Street has been out for over a week. It makes the street very dark at night and feels unsafe for pedestrians.",
            status="resolved",
        )
        Feedback.objects.create(
            type="complaint",
            name="Elena Rodriguez",
            email="elena.r@riverside.com",
            category="other",
            message="There is a massive pile of construction waste dumped right near the north entrance of Riverside Park. It's blocking the bike path and looks terrible.",
            status="flagged",
        )
        Feedback.objects.create(
            type="suggestion",
            name="Arthur Dent",
            email="adent@galaxy.com",
            category="environment",
            message="Implementing IoT sensors in public garbage bins could save the city thousands in fuel costs by ensuring garbage trucks only stop when bins are actually full.",
            status="in_review",
        )

        NewsArticle.objects.create(
            title="Town Hall: Shaping the Future Together",
            content="Our recent town hall gathered over 500 citizens to discuss local infrastructure needs and the new unity initiative.",
            tags="Community",
            category="Community",
            image_url="https://lh3.googleusercontent.com/aida-public/AB6AXuAXHoGWc-mEwjUc9iYXV1wFrFxAysQqGzbvG51bqiqnNqJI9AdB7Pg79TCocHavVwXjniU2lyIUiaHz6HiVmHw1_N3dEIkxDiFwi9GefX6apWu7Y3RueQMGPLy29xp_r5TQPL6sD5MvpX0CftKKnvxPRFBcTrRShCGDEhXoHPU77e-i0_Hqg9rEZjWIMv1VA3JAr2q-5WiZkafHDwx_3jLOfdjO_SAShlPde_1qYRLhCpJPxoKoDtIR",
            views=1200,
            likes=450,
        )
        NewsArticle.objects.create(
            title="Tax Reform Proposal Released",
            content="Chair James Sterling unveils the party's comprehensive tax relief package designed to support the middle class.",
            tags="Policy",
            category="Policy",
            image_url="https://lh3.googleusercontent.com/aida-public/AB6AXuC6_lAckKFVnmhObzle7xs3A_ENMXSKzpsz9asrq4ozVBSnRmIy4cCNDpEs6vdXJbf7eejZAexkU9_H8Q_FI03TZXd5SZnJBLSrO5oRnHnSV9wnSsuIvjULfTSHKi5JFXaudmXlUdFIqZ6_pm4JIMkxrIfoPl0mFbz7qFPwCdsUSyRTPVegij4k7tl5kQYwK2Taj_dA0HomlbySB0Z8Jf6PlFxdxGTzbKse-b_TB_S3Sb3khuDSDrnn",
            views=890,
            likes=210,
        )
        NewsArticle.objects.create(
            title="Economic Growth Report: Positive Trends",
            content="New quarterly data shows our initiatives are driving job creation and market confidence across several key sectors.",
            tags="Economy",
            category="Economy",
            image_url="https://lh3.googleusercontent.com/aida-public/AB6AXuAWxmJueiRpbIoIiyM9AiX6-HMpVJA8cMHbO7TaiNmHOcEaUWOMbHzUe1K7XlvV66ifRp9M98zDRYYtwpCi7_6UU05ZkEkXNiCXMuqG7rYSXGrA_mvbj-WJih_KXcPsU1KGSrkcgLy4kJzsLTZ53_xk-E115kvizUgnpECURXDopDMeq-WTBeGjZgfHJ0l_t7Sf_LSiQmL4YtGHpVgk_wNuuosuD8_GdICtt2l9r0P88D0e911DgdUh",
            views=670,
            likes=98,
        )

        self.stdout.write(self.style.SUCCESS("Seed data created."))
