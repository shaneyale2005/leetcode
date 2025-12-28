import unittest
import random

from bubble_sort import bubble_sort

class TestSorting(unittest.TestCase):

    def check_sort(self, sort_func):
        
        test_inputs = [
            [],                         
            [1],                        
            [0],                        
            [-1],                       
            [1, 2],                     

            [2, 1],                     
            [1, 2, 3, 4, 5],            
            [5, 4, 3, 2, 1],            
            [1, 3, 2],                  
            [100, 1, 50],               

            [1, 1],                     
            [1, 1, 1, 1, 1],            
            [1, 2, 1],                  
            [2, 1, 1],                  
            [1, 1, 2],                  
            [3, 3, 1, 1, 2, 2],         
            [1, 2, 3, 1, 2, 3],         
            [0, 0, 0, 1, 0],            
            [5, 2, 9, 1, 5, 6],         
            [1, 0, 0, 0, 1],            

            [-1, -2, -3],               
            [-3, -2, -1],               
            [-1, 0, 1],                 
            [1, 0, -1],                 
            [-5, 5, 0],                 
            [0, -1, -5, 2, 4],          
            [-100, -200, -1],           
            [10, -10, 5, -5],           
            [0, 0, -1, 1],              
            [-1, -1, 2, 2],             

            [0.5, 0.2, 0.8],            
            [1.1, 1.01, 1.001],         
            [-0.5, 0.5, 0.0],           
            [3.14, 2.71, 1.41],         
            [10.0, 10, 9.9],            

            [1, 3, 5, 2, 4, 6],         
            [1, 10, 2, 9, 3, 8],        
            [1, 2, 4, 8, 16, 32],       
            [1000, 0, -1000],           
            [21, 12, 21, 12],           

            [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],  
            [9, 8, 7, 6, 5, 5, 4, 3, 2, 1, 0],  
            [1, 3, 5, 7, 9, 0, 2, 4, 6, 8],     
            list(range(20)),                    
            list(range(20, 0, -1)),             
            [random.randint(-50, 50) for _ in range(10)], 
            [random.randint(-50, 50) for _ in range(15)], 
            [random.randint(-50, 50) for _ in range(20)], 
            [random.randint(0, 1) for _ in range(20)],    
            [random.randint(1, 1000) for _ in range(8)],  
        ]

        for i, nums in enumerate(test_inputs):
            with self.subTest(case_index=i, input=nums):
                data = nums.copy()          
                expected = sorted(nums)     
                
                sort_func(data)
                
                self.assertEqual(data, expected, f"Failed on input: {nums}")

    def test_bubble_sort(self):
        self.check_sort(bubble_sort)

if __name__ == "__main__":
    unittest.main()
