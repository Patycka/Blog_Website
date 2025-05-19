from datetime import date
from django.shortcuts import render

all_posts = [
    {
        "slug": "healthy-sleep",
        "image": "healthy_sleep.jpg",
        "author": "Patrycja P",
        "date": date(2025, 5, 10),
        "title": "Healthy Sleep",
        "excerpt": "Getting 7–9 hours of quality sleep each night is \
                            essential for your body and mind.",
        "content": """
        Getting 7–9 hours of quality sleep each night is essential for your body and mind. 
        During sleep, your body undergoes crucial processes such as tissue repair, muscle 
        growth, and the consolidation of memories. Adequate sleep helps regulate hormones, 
        strengthens the immune system, and supports cognitive functions like focus, 
        problem-solving, and emotional regulation. On the other hand, chronic sleep 
        deprivation can lead to mood disorders, weakened immunity, weight gain, and 
        increased risk of serious health conditions such as heart disease and diabetes. 
        Prioritizing restful sleep is one of the most effective ways to enhance your 
        overall health, productivity, and well-being.
        """
    },
    {
        "slug": "sugar-truth",
        "image": "sugar.jpg",
        "author": "Patrycja P",
        "date": date(2025, 5, 11),
        "title": "The Truth About Sugar: How Much Is Too Much?",
        "excerpt": '''According to the World Health Organization (WHO), the recommended daily limit 
        for added sugar is no more than 10'%' of your total daily energy intake''',
        "content": """
        Sugar is everywhere — in our morning coffee, packaged snacks, sauces, and even so-called "healthy" foods. While our bodies need a small amount of natural sugar (like the kind found in fruits and dairy), added sugar can be a silent saboteur of health.
        So, how much is too much?
        According to the World Health Organization (WHO), the recommended daily limit for added sugar is no more than 10'%' of your total daily energy intake, with a further benefit if it's reduced to 5%. For most adults, that's around:
        25 grams (6 teaspoons) per day for women 36 grams (9 teaspoons) per day for men. Unfortunately, many people consume more than double that amount without realizing it — thanks to sugary drinks, cereals, desserts, and processed foods.
        """
    },
    {
        "slug": "walking",
        "image": "walking.jpg",
        "author": "Patrycja P",
        "date": date(2025, 5, 12),
        "title": "The Truth About Sugar: How Much Is Too Much?",
        "excerpt": '''Walking is one of the simplest, most underrated forms of 
        exercise — yet its benefits are powerful.''',
        "content": """
        Walking is one of the simplest, most underrated forms of exercise — yet its benefits 
        are powerful. Whether you're strolling around the block or speed-walking through 
        the park, adding more steps to your day can have a major impact on your overall health.
        
        Why walking matters
        Walking isn’t just “better than nothing” — it’s a full-fledged form of cardiovascular
        exercise that can help:
        Burn calories and support weight management
        Improve heart health and circulation
        Reduce stress and anxiety
        Boost mood and energy levels
        Strengthen muscles and joints
        Improve digestion and sleep
        How many steps do you really need?
        You’ve probably heard the magic number: 10,000 steps a day. While it’s a good goal,
        research shows that even 6,000–8,000 steps can significantly reduce the risk of 
        early death in adults. The key is consistency and gradually increasing your step 
        count over time.
        """
    }
]

def get_date(post):
    return post.get('date')


# Create your views here.
def main_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    # latest_posts = 
    return render(request, 'blog/index.html', {"posts": latest_posts})

def posts(request):
    sorted_posts = sorted(all_posts, key=get_date)
    return render(request, 'blog/all-posts.html', {"posts": sorted_posts})

def show_post(request, slug):
    return render(request, 'blog/post-detail.html')