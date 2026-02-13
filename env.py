import os

os.environ.setdefault(
    "DATABASE_URL", "postgresql://neondb_owner:npg_L0aQiVCgOIk9@ep-wild-sun-agotoq8v.c-2.eu-central-1.aws.neon.tech/stall_swing_stool_819339")

os.environ["STRIPE_PUBLISHABLE_KEY"] = "pk_test_51SvzCtLmyIXXC8QP3HPgwnUkVKGug4t943o6BXs5s4wiP4jGkqI3hm4M30dR4o7spMfTLTenvwcbUjwffKc3J8R40065fa2jYO"
os.environ["STRIPE_SECRET_KEY"] = "sk_test_51SvzCtLmyIXXC8QPEkjF7jqcudTRDckN4TnX6C4NiaxLxqqnhRHZCfAzHeNwNUKsCgYsyzCeFV0oO3SNsDc2ljHN00mapsqiqw"
os.environ["SECRET_KEY"] = 'django-insecure-cbaqhvgegpjkrmdvua7yh0+nhf(7f$0jof5!65+yk7qde^$p^+'