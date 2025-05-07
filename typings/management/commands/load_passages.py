from django.core.management.base import BaseCommand
from typings.models import TextPassage

class Command(BaseCommand):
    help = 'Loads sample typing passages into the database'
    
    def handle(self, *args, **kwargs):
        passages = [
            {
                'content': 'The quick brown fox jumps over the lazy dog. This sentence contains all the letters in the English alphabet.',
                'difficulty': 'easy'
            },
            {
                'content': 'Programming is the process of creating a set of instructions that tell a computer how to perform a task. Programming can be done using a variety of computer programming languages.',
                'difficulty': 'medium'
            },
            {
                'content': 'The juxtaposition of quantum mechanics and general relativity presents a conundrum that has perplexed physicists for decades, necessitating a paradigm shift in our fundamental understanding of spacetime continuum.',
                'difficulty': 'hard'
            }
        ]
        
        for passage in passages:
            TextPassage.objects.create(
                content=passage['content'],
                difficulty=passage['difficulty']
            )
        
        self.stdout.write(self.style.SUCCESS('Successfully loaded sample passages'))