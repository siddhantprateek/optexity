# Documentation Writing Standards

## Core Principles

Write clear, concise documentation that helps users accomplish their goals. Focus on practical examples and real-world usage patterns.

## Page Structure

### Title and Description

Start each page with a clear title and brief description (1-2 sentences) that explains what the page covers.

### Section Organization

Use descriptive section headers without numbers. Organize content hierarchically using proper markdown heading levels (##, ###, ####).

**Correct:**

```markdown
## Getting Started

### Installation

### Configuration
```

**Incorrect:**

```markdown
## 1. Getting Started

### 1.1 Installation
```

## Content Components

### When to Use Lists

**Unordered Lists** - Use for items without inherent order or ranking:

```markdown
<ul>
  <li>Feature description</li>
  <li>Another feature</li>
</ul>
```

**Ordered Lists** - Use for sequential steps, rankings, or prioritized items:

```markdown
<ol>
  <li>First step</li>
  <li>Second step</li>
</ol>
```

**Guidelines:**

- Use lists sparingly, only when they improve clarity
- Keep list items concise (1-3 sentences maximum)
- Avoid nested lists deeper than 2 levels

### Steps Component

Use `<Steps>` for sequential tutorials or multi-step processes where order matters critically.

```markdown
<Steps>
  <Step title="Install the package">
    Run `npm install package-name` in your terminal.
  </Step>
  
  <Step title="Configure your environment">
    Add your API key to `.env` file.
  </Step>
  
  <Step title="Initialize the client">
    Import and configure the client in your application.
  </Step>
</Steps>
```

**When to use:**

- Installation guides with multiple dependencies
- Multi-step setup processes
- Configuration walkthroughs
- Onboarding tutorials

**When NOT to use:**

- Simple single-step instructions
- Conceptual explanations
- Reference documentation

### Info Callouts

Use `<Info>` for helpful context that enhances understanding but isn't critical.

```markdown
<Info>
  This feature is available in Pro and Enterprise plans.
</Info>
```

**When to use:**

- Plan availability information
- Version compatibility notes
- Additional context that aids understanding
- Non-critical supplementary information

**Limit:** Maximum 1-2 per page

### Tip Callouts

Use `<Tip>` for best practices, optimization suggestions, or expert advice.

```markdown
<Tip>
  For better performance, enable caching in production environments.
</Tip>
```

**When to use:**

- Performance optimization advice
- Best practices and recommendations
- Pro tips that improve user experience
- Common shortcuts or time-savers

**Limit:** Maximum 2-3 per page

### Warning Callouts

Use `<Warning>` for critical information about potential issues, breaking changes, or important caveats.

```markdown
<Warning>
  This action is irreversible and will permanently delete all data.
</Warning>
```

**When to use:**

- Destructive actions
- Breaking changes
- Security considerations
- Data loss risks

**Use sparingly:** Only for genuinely critical information

### Accordions

Use `<AccordionGroup>` to organize optional or advanced content that would otherwise clutter the page.

```markdown
<AccordionGroup>
  <Accordion title="Advanced configuration options">
    Content about advanced settings...
  </Accordion>
  
  <Accordion title="Troubleshooting common issues">
    Solutions to frequent problems...
  </Accordion>
</AccordionGroup>
```

**When to use:**

- Advanced configuration options
- Troubleshooting sections
- Optional deep-dive content
- Framework-specific variations

**When NOT to use:**

- Essential information users need upfront
- Quick start guides
- Basic setup instructions

### Card Groups

Use `<CardGroup>` to present multiple related options or paths forward.

```markdown
<CardGroup cols={2}>
  <Card title="Quick Start" icon="bolt" href="/quickstart">
    Get up and running in 5 minutes
  </Card>
  
  <Card title="Detailed Guide" icon="book" href="/guide">
    Comprehensive walkthrough with examples
  </Card>
</CardGroup>
```

**When to use:**

- Navigation between related guides
- Presenting integration options
- Showcasing multiple approaches
- Feature overviews with links

**Limit:** Use 2-4 cards per group for optimal readability

## Code Examples

### Code Blocks

Always specify the language for syntax highlighting:

````markdown
```javascript
const client = new APIClient({ apiKey: "your-key" });
```
````

````

### Inline Code

Use backticks for inline code, commands, file names, and variable names:

```markdown
Install the package with `npm install` and configure your `API_KEY` variable.
````

### Code Tabs

For multi-language examples, use code tabs:

````markdown
<CodeGroup>
```javascript
// JavaScript example
const result = await client.query();
````

```python
# Python example
result = client.query()
```

</CodeGroup>
```

## Writing Style

### Voice and Tone

- Write in second person ("you") to address the reader directly
- Use active voice instead of passive voice
- Keep sentences clear and concise
- Avoid jargon unless necessary, then define it

### Technical Accuracy

- Test all code examples before publishing
- Include complete, runnable code snippets when possible
- Specify version requirements when relevant
- Update examples when APIs change

### Consistency

- Use consistent terminology throughout documentation
- Follow established naming conventions
- Maintain uniform code style across examples
- Apply the same structure to similar pages

## Avoid Overuse

**Do not:**

- Stack multiple callouts consecutively
- Use callouts for every paragraph
- Create accordion groups with single items
- Nest components unnecessarily
- Over-format with bold and italics

**Remember:** Components enhance documentation when used purposefully. Plain prose is often the clearest choice.
