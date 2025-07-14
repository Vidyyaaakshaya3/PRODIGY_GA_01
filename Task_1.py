# 🎬 CLEAN MOVIE RECOMMENDATION SYSTEM 🎬

print("🎬 MOVIE RECOMMENDATION SYSTEM 🎬")
print("=" * 50)
print("✨ Get clean, easy-to-read movie recommendations!")
print("=" * 50)

def clean_movie_recommender():
    """Clean, minimalistic movie recommendation interface"""

    print("\n🎯 POPULAR SEARCHES:")
    print("• action movies    • horror movies    • comedy movies")
    print("• sci-fi films     • romance movies   • thriller movies")
    print("• drama movies     • animated movies  • adventure movies")

    print("\n💡 TIP: Try adding years like 'action movies from 1990s'")
    print("=" * 50)

    while True:
        try:
            # Get user input
            user_request = input("\n🎬 What movies do you want? (or 'quit'): ").strip()

            # Check if user wants to quit
            if user_request.lower() in ['quit', 'exit', 'stop', 'q']:
                print("\n👋 Thanks for using the system!")
                break

            # Check if input is empty
            if not user_request:
                print("🤔 Please tell me what movies you want!")
                continue

            # Get recommendations
            print(f"\n🎯 RECOMMENDATIONS FOR: {user_request.upper()}")
            print("=" * 50)

            recommendations = model.generate_recommendation(user_request)

            # Extract and display clean movie info
            movies_found = []
            for rec in recommendations:
                # Try to extract movie information from generated text
                text = rec.lower()

                # Look for movie patterns in our training data
                for _, row in movie_df.iterrows():
                    movie_title = row['title'].lower()
                    if movie_title in text:
                        movie_info = {
                            'title': row['title'],
                            'year': row['year'],
                            'genres': row['genres'].replace(',', ' • ')
                        }
                        if movie_info not in movies_found:
                            movies_found.append(movie_info)
                        break

            # If we found specific movies, display them cleanly
            if movies_found:
                for i, movie in enumerate(movies_found[:3], 1):
                    print(f"🎬 {i}. {movie['title']} ({movie['year']})")
                    print(f"   📁 {movie['genres']}")
                    print()
            else:
                # Fallback: show clean AI-generated recommendations
                print("🤖 AI SUGGESTIONS:")
                for i, rec in enumerate(recommendations[:3], 1):
                    # Clean up the generated text
                    clean_text = rec.split('?')[1] if '?' in rec else rec
                    clean_text = clean_text.replace('I recommend', '').replace('try', '').replace('watch', '')
                    clean_text = clean_text.strip().strip(',').strip('.')
                    if clean_text:
                        print(f"🎬 {i}. {clean_text}")
                print()

            print("=" * 50)
            print("💡 Want more? Just type another movie type!")

        except KeyboardInterrupt:
            print("\n\n👋 Thanks for using the system!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
            print("🔄 Try again with a simpler request!")

# 🚀 START THE CLEAN SYSTEM
print("\n🚀 Starting Clean Movie Recommendation System...")

# Call the clean function
clean_movie_recommender()

print("\n🎉 Session ended! Run again for more recommendations!")
