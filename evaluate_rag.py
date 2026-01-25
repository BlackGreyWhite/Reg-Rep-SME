"""
Simple RAG evaluation script
Tests accuracy, relevance, and hallucination detection
"""

import os
from chat_with_knowledge import chat_with_rag

# Test cases: questions you know the answers to
TEST_CASES = [
    {
        "question": "What topics are covered in the Securities and Futures regulations?",
        "expected_keywords": ["securities", "futures", "derivatives", "reporting", "regulation"],
        "should_answer": True
    },
    {
        "question": "What is the recipe for chocolate chip cookies?",
        "expected_keywords": ["don't have", "no information"],
        "should_answer": False
    },
    {
        "question": "What regulations does MAS enforce?",
        "expected_keywords": ["mas", "regulation", "financial", "monetary"],
        "should_answer": True
    },
    {
        "question": "What are the derivatives reporting requirements?",
        "expected_keywords": ["derivatives", "reporting", "requirements"],
        "should_answer": True
    }
]

def evaluate():
    """Run evaluation tests"""
    print("="*80)
    print("RAG SYSTEM EVALUATION")
    print("="*80)
    
    passed = 0
    failed = 0
    
    for i, test in enumerate(TEST_CASES, 1):
        print(f"\n[Test {i}/{len(TEST_CASES)}] {test['question']}")
        print("-" * 80)
        
        try:
            # Get answer (suppress source printing)
            answer = chat_with_rag(test['question'], show_sources=False)
            
            # Check if answer contains expected keywords
            answer_lower = answer.lower()
            keyword_found = any(kw.lower() in answer_lower for kw in test['expected_keywords'])
            
            # Determine if test passed
            if test['should_answer']:
                # Should give a real answer with expected keywords
                if keyword_found and len(answer) > 50:
                    print("✅ PASS: Found expected content")
                    passed += 1
                else:
                    print("❌ FAIL: Missing expected keywords or answer too short")
                    print(f"   Answer: {answer[:100]}...")
                    failed += 1
            else:
                # Should refuse to answer
                if keyword_found:
                    print("✅ PASS: Correctly refused to answer")
                    passed += 1
                else:
                    print("❌ FAIL: Should have refused but gave an answer")
                    print(f"   Answer: {answer[:100]}...")
                    failed += 1
                    
        except Exception as e:
            print(f"❌ ERROR: {e}")
            failed += 1
    
    # Summary
    print("\n" + "="*80)
    print("EVALUATION SUMMARY")
    print("="*80)
    print(f"Total Tests: {len(TEST_CASES)}")
    print(f"Passed: {passed} ({passed/len(TEST_CASES)*100:.0f}%)")
    print(f"Failed: {failed} ({failed/len(TEST_CASES)*100:.0f}%)")
    
    if passed == len(TEST_CASES):
        print("\n🎉 All tests passed! Your RAG system is working well.")
    elif passed >= len(TEST_CASES) * 0.7:
        print("\n⚠️  Most tests passed, but some issues found. Review failed tests.")
    else:
        print("\n❌ Many tests failed. Review your system configuration.")
    
    return passed, failed

if __name__ == "__main__":
    evaluate()