import functools
import time

# -----------------------------------------
# Decorator 1: Logging
# -----------------------------------------
def log(func):
    """
    Logs function calls and execution time.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f"[LOG] Calling: {func.__name__}")
        
        result = func(*args, **kwargs)
        
        end = time.time()
        print(f"[LOG] Finished: {func.__name__} | Time: {end - start:.4f}s")
        return result

    return wrapper


# -----------------------------------------
# Decorator 2: Caching (simple memoization)
# -----------------------------------------
def cache(func):
    """
    Caches results of function calls to avoid recomputation.
    """
    memo = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args in memo:
            print("[CACHE] Returning cached result")
            return memo[args]

        print("[CACHE] No cache, computing...")
        result = func(*args)
        memo[args] = result
        return result

    return wrapper


# -----------------------------------------
# Base Function (to enhance)
# -----------------------------------------
@log        # Decorator 1
@cache      # Decorator 2
def predict(frame):
    """
    Base prediction function.
    In a real system, this would call the model inference.
    """
    # Fake heavy computation
    time.sleep(1)
    return f"Prediction result for {frame}"


# -----------------------------------------
# Example Usage
# -----------------------------------------
if __name__ == "__main__":
    print(predict("frame_001"))  # First call → compute + log + cache
    print("\n--- Calling again ---\n")
    print(predict("frame_001"))  # Second call → cached + log (still logged)
