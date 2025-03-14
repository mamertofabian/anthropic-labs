import anthropic

from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-3-7-sonnet-20250219",
    max_tokens=20000,
    temperature=0.6,
    system="You are an expert QA engineer specializing in writing comprehensive Gherkin test cases for software applications. Focus on creating test cases that cover all functional requirements and important edge cases.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Requirements:\n- User Authentication System: Implement comprehensive authentication flows including registration, login, password reset, and social logins (Google, GitHub) through Supabase Auth. The system should maintain session state and handle token refresh automatically.\n- Role-Based Access Control: Provide differentiated access levels for regular users and administrators. Admin users should have access to user management functionalities and system settings, while regular users should only access their own data and profile.\n- Data Management Operations: Support complete CRUD operations for application items, with appropriate validation, error handling, and real-time updates. Items should be user-scoped to ensure data privacy.\n- User Profile Management: Allow users to view and update their profile information, including personal details, preferences, and account settings. Profile changes should be persisted to the database immediately.\n- Admin Dashboard & Analytics: Provide administrators with a dashboard showing key metrics, user statistics, and system health indicators. Include user management tools with the ability to view, edit, and manage user accounts.\n- Security: Implement proper authentication mechanisms, data encryption, protection against common web vulnerabilities (XSS, CSRF, SQL injection), and secure API access. Follow security best practices for handling user data and credentials.\n- Performance: Ensure application responsiveness with page load times under 2 seconds, efficient database queries, and optimized frontend rendering. Implement caching strategies for frequently accessed data.\n- Usability & Accessibility: Create a responsive interface that works across desktop and mobile devices. Follow WCAG 2.1 AA standards for accessibility, ensuring the application is usable by people with various disabilities.\n- Scalability: Design the application to handle increasing user loads without performance degradation. Implement database indexing strategies and optimize query patterns for large datasets.\n- Maintainability: Structure code with clear organization, consistent naming conventions, and comprehensive documentation. Implement testing at unit, integration, and E2E levels to ensure code quality and facilitate future changes.\n\nFeatures:\n[\n  {\n    \"name\": \"Authentication & Security\",\n    \"description\": \"Secure user authentication, authorization, and data protection features\",\n    \"enabled\": true,\n    \"optional\": false,\n    \"providers\": [\n      \"Firebase\"\n    ]\n  },\n  {\n    \"name\": \"User Management\",\n    \"description\": \"Profile management, family member accounts, and user preferences\",\n    \"enabled\": true,\n    \"optional\": false,\n    \"providers\": null\n  },\n  {\n    \"name\": \"Transaction Management\",\n    \"description\": \"Core functionality for recording, categorizing, and managing daily financial transactions\",\n    \"enabled\": true,\n    \"optional\": false,\n    \"providers\": null\n  },\n  {\n    \"name\": \"Budget Planning\",\n    \"description\": \"Tools for creating, managing, and tracking family budgets across categories\",\n    \"enabled\": true,\n    \"optional\": false,\n    \"providers\": null\n  },\n  {\n    \"name\": \"Financial Dashboard\",\n    \"description\": \"Overview of financial health with key metrics and visualizations\",\n    \"enabled\": true,\n    \"optional\": false,\n    \"providers\": null\n  },\n  {\n    \"name\": \"Administration\",\n    \"description\": \"System administration tools for managing users, system health, and application settings\",\n    \"enabled\": true,\n    \"optional\": false,\n    \"providers\": null\n  }\n]\n\nYour task:\n1. Create comprehensive test cases using Gherkin format (Feature, Scenario, Given, When, Then)\n2. Each test case should include:\n   * Feature name\n   * Test case title\n   * Optional description\n   * Optional tags (like @smoke, @regression, @ui, @api)\n   * One or more scenarios with steps using Given/When/Then\n3. Cover both happy paths and edge cases\n4. Ensure all critical requirements are addressed by test cases\n5. If the user provided original test cases, enhance them by:\n   * Improving steps to be more specific and precise\n   * Adding missing scenarios\n   * Adding appropriate tags\n   * Organizing them into logical features\n6. If generating from scratch, create test cases that comprehensively verify requirements\n\nOnce you've analyzed the requirements and features, use the print_test_cases function to output the organized test cases."
                }
            ]
        }
    ],
    tools=[
        {
            "name": "print_test_cases",
            "description": "Formats and displays the organized test cases using Gherkin format",
            "input_schema": {
                "type": "object",
                "properties": {
                    "data": {
                        "type": "object",
                        "description": "The structured test cases data",
                        "properties": {
                            "testCases": {
                                "type": "array",
                                "description": "List of test cases in Gherkin format",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "feature": {
                                            "type": "string",
                                            "description": "The feature being tested (e.g., User Authentication, Shopping Cart)"
                                        },
                                        "title": {
                                            "type": "string",
                                            "description": "Title of the test case (e.g., Login with valid credentials)"
                                        },
                                        "description": {
                                            "type": "string",
                                            "description": "Optional description of the test case"
                                        },
                                        "tags": {
                                            "type": "array",
                                            "description": "Optional tags for categorizing the test case (e.g., smoke, regression, ui)",
                                            "items": {
                                                "type": "string"
                                            }
                                        },
                                        "scenarios": {
                                            "type": "array",
                                            "description": "List of scenarios in this test case",
                                            "items": {
                                                "type": "object",
                                                "properties": {
                                                    "name": {
                                                        "type": "string",
                                                        "description": "Name of the scenario (e.g., Successful login, Invalid credentials)"
                                                    },
                                                    "steps": {
                                                        "type": "array",
                                                        "description": "Gherkin steps (Given/When/Then/And/But)",
                                                        "items": {
                                                            "type": "object",
                                                            "properties": {
                                                                "type": {
                                                                    "type": "string",
                                                                    "enum": [
                                                                        "given",
                                                                        "when",
                                                                        "then",
                                                                        "and",
                                                                        "but"
                                                                    ],
                                                                    "description": "Type of step"
                                                                },
                                                                "text": {
                                                                    "type": "string",
                                                                    "description": "Text of the step (e.g., the user enters valid credentials)"
                                                                }
                                                            },
                                                            "required": [
                                                                "type",
                                                                "text"
                                                            ]
                                                        }
                                                    }
                                                },
                                                "required": [
                                                    "name",
                                                    "steps"
                                                ]
                                            }
                                        }
                                    },
                                    "required": [
                                        "feature",
                                        "title",
                                        "scenarios"
                                    ]
                                }
                            }
                        },
                        "required": [
                            "testCases"
                        ]
                    }
                },
                "required": [
                    "data"
                ]
            }
        }
    ]
)

print(message.content)
